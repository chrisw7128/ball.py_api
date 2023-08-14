import json

from ball import models
from flask import Blueprint, render_template, request, redirect

reptile_bp = Blueprint("reptile_bp", __name__, url_prefix="/reptiles")


@reptile_bp.route("/")
def index():
    return "This is the reptiles index."


@reptile_bp.route("/new")
def get_post():
    return "New reptile details"
