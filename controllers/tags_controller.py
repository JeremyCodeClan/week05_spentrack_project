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