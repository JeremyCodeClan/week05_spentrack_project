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
    pass

def select(id):
    pass

def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)

def delete(id):
    pass

def update(tag):
    pass