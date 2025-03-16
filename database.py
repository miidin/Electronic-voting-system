from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Voter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(15), unique=True, nullable=False)
    has_voted = db.Column(db.Boolean, default=False)

def init_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///votes.db"
    db.init_app(app)
    with app.app_context():
        db.create_all()  # Create database tables
