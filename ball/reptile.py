import json

from flask import Blueprint, render_template, request, redirect
from .models import Reptile, db

reptile_bp = Blueprint("reptile_bp", __name__, url_prefix="/reptiles")


@reptile_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print(request.form)
        submitter = request.form["submitter"]
        reptile_id = request.form["reptile_id"]
        reptile_name = request.form["reptile_name"]
        reptile_fact = request.form["reptile_fact"]

        new_reptile = Reptile(id=reptile_id, name=reptile_name, fact=reptile_fact)
        db.session.add(new_reptile)
        db.session.commit()

        return redirect("/reptiles")

    # rows = model.Reptile.query.all()

    reptiles = json.load(open("reptiles.json"))
    return render_template("index.html", reptiles=reptiles)


@reptile_bp.route("/<int:id>")
def show(id):
    reptile = Reptile.query.filter_by(reptile_id=id).first()
    user_dict = {"reptile": reptile.id}
    return "New reptile details"
