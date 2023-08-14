from flask import Blueprint
from app import db

post_bp = Blueprint("post_bp", __name__)


@post_bp.route("/posts")
def list_posts():
    return "List of posts"


@post_bp.route("/post/<int:post_id>")
def get_post(post_id):
    return f"Post {post_id} details"
