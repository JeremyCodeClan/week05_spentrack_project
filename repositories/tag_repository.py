from db.run_sql import run_sql
from models.tag import Tag

def save(tag):
    sql = "INSERT INTO tags (name, count) VALUES (%s, %s) RETURNING *"
    values = [tag.name, 0]
    results = run_sql(sql, values)
    id = results[0]['id']
    tag.id = id

def select_all():
    tags = []
    sql = "SELECT * FROM tags ORDER BY count DESC"
    results = run_sql(sql)
    for row in results:
        tag = Tag(row['name'], row['count'], row['id'])
        tags.append(tag)
    return tags

def select(id):
    if id == "None" or None:
        return None
    sql = "SELECT * FROM tags WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    tag = Tag(result['name'], result['count'], result['id'])
    return tag

def delete_all():
    sql = "DELETE FROM tags"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM tags WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(tag):
    sql = "UPDATE tags SET (name, count) = (%s, %s)  WHERE id = %s"
    values = [tag.name, tag.count, tag.id]
    run_sql(sql, values)
