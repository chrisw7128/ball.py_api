from . import create_app


from blueprints.user_bp import user_bp
from blueprints.post_bp import post_bp

app.register_blueprint(user_bp, url_prefix="/users")
app.register_blueprint(post_bp, url_prefix="/posts")


app = create_app()


# Define your models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Post {self.title}>"


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run()
