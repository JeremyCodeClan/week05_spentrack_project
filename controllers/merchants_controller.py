from flask import Blueprint, Flask, render_template, request, redirect

from models.merchant import Merchant
import repositories.transaction_repository as transaction_repo
import repositories.merchant_repository as merchant_repo
import repositories.tag_repository as tag_repo

merchants_blueprint = Blueprint("merchants", __name__)


@merchants_blueprint.route("/jeremy_e51/merchants")
def merchants():
    merchants = merchant_repo.select_all()
    return render_template("merchants/index.html", merchants = merchants, login = 1)

@merchants_blueprint.route("/jeremy_e51/merchants/new")
def new():
    merchants = merchant_repo.select_all()
    return render_template(
        "merchants/new.html", 
        merchants = merchants, login = 1, new_cancel = 1
        )

@merchants_blueprint.route("/jeremy_e51/merchants", methods=['POST'])
def add_merchant():
    name = request.form['name']
    merchant = Merchant(name)
    merchant_repo.save(merchant)
    return redirect('/jeremy_e51/merchants')

@merchants_blueprint.route("/jeremy_e51/merchants/<id>")
def show_merchant(id):
    merchants = merchant_repo.select_all()
    found_transactions = transaction_repo.select_by_merchant(id)
    return render_template(
        "merchants/index.html",
        merchants = merchants, found_transactions = found_transactions, login = 1, id = int(id)
    )
