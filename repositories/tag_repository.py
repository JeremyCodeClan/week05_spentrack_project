from db.run_sql import run_sql
from models.tag import Tag

def save(tag):
    sql = "INSERT INTO tags (name) VALUES (%s) RETURNING *"
    values = [tag.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    tag.id = id

def select_all():
    pass

def select(id):
    pass

def delete_all():
    pass

def delete(id):
    pass

def update(tag):
    pass
