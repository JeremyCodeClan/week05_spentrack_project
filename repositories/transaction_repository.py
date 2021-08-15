from db.run_sql import run_sql
from models.transaction import Transaction
import repositories.merchant_repository as merchant_repo
import repositories.tag_repository as tag_repo

def save(transaction):
    sql = "INSERT INTO transactions (name, description, amount, tag_id, merchant_id) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    tag_id = None
    merchant_id = None
    if transaction.tag != None: tag_id = transaction.tag.id
    if transaction.merchant != None: merchant_id = transaction.merchant.id    
    values = [transaction.name, transaction.description, transaction.amount, tag_id, merchant_id]
    result = run_sql(sql, values)
    id = result[0]['id']
    transaction.id = id

def select_all():
    transactions = []
    sql = "SELECT * FROM transactions ORDER BY id DESC"
    results = run_sql(sql)
    for row in results:
        tag = None
        merchant = None
        if row['tag_id'] != None: tag = tag_repo.select(row['tag_id'])
        if row['merchant_id'] != None: merchant = merchant_repo.select(row['merchant_id'])
        transaction = Transaction(
            row['name'], row['description'],
            row['amount'], tag,
            merchant, row['id']
            )
        transactions.append(transaction)
    return transactions

def select(id):
    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    transaction = Transaction(
            result['name'], result['description'],
            result['amount'], result['tag_id'],
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
    sql = "UPDATE transactions SET (name, description, amount, tag_id, merchant_id) = (%s, %s, %s, %s, %s) WHERE id = %s"
    tag_id = None
    merchant_id = None
    if transaction.tag != None: tag_id = transaction.tag.id
    if transaction.merchant != None: merchant_id = transaction.merchant.id   
    values = [transaction.name, transaction.description, transaction.amount, tag_id, merchant_id, transaction.id]
    run_sql(sql, values)