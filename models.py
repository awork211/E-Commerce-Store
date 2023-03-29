from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))

    def __init__(self, email, password, first_name):
        self.email = email
        self.password = password
        self.first_name = first_name

class Inventory(db.Model):
    __tablename__ = 'inventory'
    item_id = db.Column(db.Integer, primary_key=True)
    image_src = db.Column(db.String(50))
    description = db.Column(db.String(300))
    price = db.Column(db.Float)
    category = db.Column(db.String(50))
