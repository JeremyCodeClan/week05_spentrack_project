from flask import Blueprint, Flask, render_template, request, redirect

from models.tag import Tag
import repositories.transaction_repository as transaction_repo
import repositories.merchant_repository as merchant_repo
import repositories.tag_repository as tag_repo

tags_blueprint = Blueprint("tags", __name__)

@tags_blueprint.route("/jeremy_e51/tags")
def tags():
    tags = tag_repo.select_all()
    return render_template("tags/index.html", tags = tags, login = 1)

@tags_blueprint.route("/jeremy_e51/tags/new")
def new():
    tags = tag_repo.select_all()
    return render_template(
        "tags/new.html", 
        tags = tags, login = 1, new_cancel = 1
    )

@tags_blueprint.route("/jeremy_e51/tags", methods=['POST'])
def add_tag():
    name = request.form['name']
    tag = Tag(name)
    tag_repo.save(tag)
    return redirect('/jeremy_e51/tags')

@tags_blueprint.route("/jeremy_e51/tags/<id>")
def show_tag(id):
    tags = tag_repo.select_all()
    found_transactions = transaction_repo.select_by_tag(id)
    return render_template(
        "tags/index.html", 
        tags = tags, found_transactions = found_transactions, login = 1, id = int(id)
    )