from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Reptile(db.Model):
    __tablename__ = "reptiles"

    reptile_id = db.Column(db.Integer, primary_key=True)
    reptile_name = db.Column(db.String(80), unique=True, nullable=False)
    reptile_fact = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, id, name, fact):
        self.id = id
        self.name = name
        self.fact = fact
