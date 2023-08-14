from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


# factory
def create_app():
    app = Flask(__name__)

    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "postgresql://postgres:2023!@localhost:5434/ball_api"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    from . import models

    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    @app.route("/")
    def hello():
        return "Hello, Flask Application Factory!"

    from blueprints.reptile_bp import reptile_bp

    app.register_blueprint(reptile_bp)

    return app
