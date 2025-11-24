from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "USER"
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    given_name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
