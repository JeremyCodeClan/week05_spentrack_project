from models.merchant import Merchant
from db.run_sql import run_sql
from models.transaction import Transaction
import repositories.merchant_repository as merchant_repo
import repositories.tag_repository as tag_repo

def reuseable_select_all(sql):
    transactions = []
    results = run_sql(sql)
    for row in results:
        tag = None
        merchant = None
        if row['tag_id'] != None: tag = tag_repo.select(row['tag_id'])
        if row['merchant_id'] != None: merchant = merchant_repo.select(row['merchant_id'])
        transaction = Transaction(
            row['name'], row['description'],
            row['amount'], row['date'], tag,
            merchant, row['id']
            )
        transactions.append(transaction)
    return transactions

def save(transaction):
    sql = "INSERT INTO transactions (name, description, amount, date, tag_id, merchant_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    tag_id = None
    merchant_id = None
    if transaction.tag != None:
        tag_id = transaction.tag.id
        tag = tag_repo.select(tag_id)
        tag.count += 1
        tag_repo.update(tag)
    if transaction.merchant != None:
        merchant_id = transaction.merchant.id
        merchant = merchant_repo.select(merchant_id)
        merchant.total += transaction.amount
        merchant_repo.update(merchant)
    values = [transaction.name, transaction.description, transaction.amount, transaction.date, tag_id, merchant_id]
    result = run_sql(sql, values)
    id = result[0]['id']
    transaction.id = id

def select_all():
    sql = "SELECT * FROM transactions ORDER BY date DESC"
    results = reuseable_select_all(sql)
    return results

def select(id):
    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    transaction = Transaction(
            result['name'], result['description'],
            result['amount'], result['date'], result['tag_id'],
            result['merchant_id'], result['id']
            )
    return transaction

def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(transaction):
    sql = "UPDATE transactions SET (name, description, amount, date, tag_id, merchant_id) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    tag_id = None
    merchant_id = None
    if transaction.merchant is not None:
        if type(transaction.merchant) != int:
            merchant_id = transaction.merchant.id
            merchant = merchant_repo.select(merchant_id)
            merchant.total += transaction.amount
            merchant_repo.update(merchant)
        else:
            merchant_id = transaction.merchant
    if transaction.tag is not None:
        if type(transaction.tag) != int:
            tag_id = transaction.tag.id
            tag = tag_repo.select(tag_id)
            tag.count += 1
            tag_repo.update(tag)
        else:
            tag_id = transaction.tag          
    values = [transaction.name, transaction.description, transaction.amount, transaction.date, tag_id, merchant_id, transaction.id]
    run_sql(sql, values)

def total_amount(transactions):
    total = 0
    for transaction in transactions:
        total += transaction.amount
    return total

def select_by_merchant(merchant_id):
    transactions = []
    sql = "SELECT * FROM transactions WHERE merchant_id = %s"
    values = [merchant_id]
    results = run_sql(sql, values)
    for row in results:
        tag = None
        if row['tag_id'] != None: tag = tag_repo.select(row['tag_id'])
        transaction = Transaction(
            row['name'], row['description'],
            row['amount'], row['date'], tag,
            None, row['id']
            )
        transactions.append(transaction)
    return transactions

def select_by_tag(tag_id):
    transactions = []
    sql = "SELECT * FROM transactions WHERE tag_id = %s"
    values = [tag_id]
    results = run_sql(sql, values)
    for row in results:
        merchant = None
        if row['merchant_id'] != None: merchant = tag_repo.select(row['merchant_id'])
        transaction = Transaction(
            row['name'], row['description'],
            row['amount'], row['date'], None,
            merchant, row['id']
            )
        transactions.append(transaction)
    return transactions

def order_by_price_desc():
    sql = "SELECT * FROM transactions ORDER BY amount DESC"
    results = reuseable_select_all(sql)
    return results

def order_by_price_asc():
    sql = "SELECT * FROM transactions ORDER BY amount ASC"
    results = reuseable_select_all(sql)
    return results
    