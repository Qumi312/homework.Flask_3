from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Reg_user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.Email, nullable=False)
    Password = db.Column(db.Password, nullable=False)
