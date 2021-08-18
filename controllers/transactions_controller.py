from flask import Blueprint, Flask, render_template, request, redirect

from models.transaction import Transaction
import repositories.transaction_repository as transaction_repo
import repositories.merchant_repository as merchant_repo
import repositories.tag_repository as tag_repo

transactions_blueprint = Blueprint("transactions", __name__)

@transactions_blueprint.route("/jeremy_e51")
def transactions():
    order = 'order_date_desc'
    transactions = transaction_repo.select_all()
    total = transaction_repo.total_amount(transactions)
    return render_template(
        "transactions/index.html", 
        transactions = transactions, total = total, login = 1, order = order
        )

@transactions_blueprint.route("/jeremy_e51/new")
def new():
    transactions = transaction_repo.select_all()
    total = transaction_repo.total_amount(transactions)
    return render_template(
        "transactions/new.html", 
        transactions = transactions, total = total, login = 1, new_cancel = 1
        )

@transactions_blueprint.route("/jeremy_e51/<id>")
def transaction_show(id):
    order = 'order_date_desc'
    show_one = transaction_repo.select(id)
    merchant = None
    tag = None
    if show_one.merchant: merchant = merchant_repo.select(show_one.merchant)
    if show_one.tag: tag = tag_repo.select(show_one.tag)
    transactions = transaction_repo.select_all()
    total = transaction_repo.total_amount(transactions)
    return render_template(
        "transactions/show.html", 
        transactions = transactions, show_one = show_one, merchant = merchant, tag = tag, total = total, login = 1, order = order
        )

@transactions_blueprint.route("/jeremy_e51", methods=['POST'])
def add_transaction():
    name = request.form['name']
    description = request.form['description']
    amount = request.form['amount']
    date = request.form['date']
    transaction = Transaction(name, description, amount, date)
    transaction_repo.save(transaction)
    return redirect('/jeremy_e51')

@transactions_blueprint.route("/jeremy_e51/<id>/edit")
def edit_transaction(id):
    transactions = transaction_repo.select_all()
    total = transaction_repo.total_amount(transactions)
    merchants = merchant_repo.select_all()
    tags = tag_repo.select_all()
    return render_template(
        'transactions/edit.html',
        transactions = transactions, merchants = merchants, tags = tags, id = int(id), total = total, login = 1
        )

@transactions_blueprint.route("/jeremy_e51/<id>", methods=['POST'])
def update_transaction(id):
    transaction = transaction_repo.select(id)

    if "tag_id" in request.form:
        if request.form["tag_id"] != "None":
            tag_id = request.form["tag_id"]
            tag = tag_repo.select(tag_id)
            transaction.tag = tag

    if "merchant_id" in request.form:
        if request.form["merchant_id"] != "None":
            merchant_id = request.form["merchant_id"]
            merchant = merchant_repo.select(merchant_id)
            transaction.merchant = merchant

    transaction_repo.update(transaction)
    return redirect('/jeremy_e51')

@transactions_blueprint.route("/jeremy_e51/order")
def transactions_by_order():
    order_date = request.args['order_date']
    order_amount = request.args['order_amount']
    order_name = request.args['order_name']
    if order_date:
        if order_date == 'desc':
            order = 'order_date_desc'
            transactions = transaction_repo.select_all()
            total = transaction_repo.total_amount(transactions)
            return render_template(
                "transactions/index.html", 
                transactions = transactions, total = total, login = 1, order = order
            )
        if order_date == 'asc':
            order = 'order_date_asc'
            transactions = transaction_repo.select_all_asc()
            total = transaction_repo.total_amount(transactions)
            return render_template(
                "transactions/index.html", 
                transactions = transactions, total = total, login = 1, order = order
            )
    if order_amount:
        if order_amount == 'desc':
            order = 'order_amount_desc'
            transactions = transaction_repo.order_by_price_desc()
            total = transaction_repo.total_amount(transactions)
            return render_template(
                "transactions/index.html", 
                transactions = transactions, total = total, login = 1, order = order
            )
        if order_amount == 'asc':
            order = 'order_amount_asc'
            transactions = transaction_repo.order_by_price_asc()
            total = transaction_repo.total_amount(transactions)
            return render_template(
                "transactions/index.html", 
                transactions = transactions, total = total, login = 1, order = order
            )
    if order_name:
        if order_name == 'desc':
            order = 'order_name_desc'
            transactions = transaction_repo.order_by_name_desc()
            total = transaction_repo.total_amount(transactions)
            return render_template(
                "transactions/index.html", 
                transactions = transactions, total = total, login = 1, order = order
            )
        if order_name == 'asc':
            order = 'order_name_asc'
            transactions = transaction_repo.order_by_name_asc()
            total = transaction_repo.total_amount(transactions)
            return render_template(
                "transactions/index.html", 
                transactions = transactions, total = total, login = 1, order = order
            )
    return redirect('/jeremy_e51')