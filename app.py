from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "postgresql://postgres:2023!@localhost:5434/ball_api"
    db = SQLAlchemy(app)

    @app.route("/")
    def hello():
        return "Hello, Flask Application Factory!"

    return app


app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run()
