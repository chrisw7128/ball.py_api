from flask import Blueprint
from app import db

user_bp = Blueprint("user_bp", __name__)


@user_bp.route("/users")
def list_users():
    return "List of users"


@user_bp.route("/user/<int:user_id>")
def get_user(user_id):
    return f"User {user_id} details"
