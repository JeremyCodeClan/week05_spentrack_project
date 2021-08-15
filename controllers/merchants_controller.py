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