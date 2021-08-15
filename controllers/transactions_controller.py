from flask import Blueprint, Flask, render_template, request, redirect

from models.transaction import Transaction
import repositories.transaction_repository as transaction_repo
import repositories.merchant_repository as merchant_repo
import repositories.tag_repository as tag_repo

transactions_blueprint = Blueprint("transactions", __name__)

@transactions_blueprint.route("/jeremy_e51")
def transactions():
    transactions = transaction_repo.select_all()
    total = transaction_repo.total_amount(transactions)
    return render_template(
        "transactions/index.html", 
        transactions = transactions, total = total, login = 1
        )

@transactions_blueprint.route("/jeremy_e51/new")
def new():
    transactions = transaction_repo.select_all()
    total = transaction_repo.total_amount(transactions)
    return render_template(
        "transactions/new.html", 
        transactions = transactions, total = total, login = 1, new_cancel = 1
        )