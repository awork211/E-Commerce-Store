from . import db
from flask_login import UserMixin
from sqlalchemy.orm import relationship
from sqlalchemy import DateTime
from datetime import datetime

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(50))

    def __init__(self, email, password, first_name):
        self.email = email
        self.password = password
        self.first_name = first_name

class Inventory(db.Model):
    __tablename__ = 'inventory'
    item_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    image_src = db.Column(db.String(50))
    description = db.Column(db.String(300))
    price = db.Column(db.Float)
    category = db.Column(db.String(50))
    item_name = db.Column(db.String(50))

class Orders(db.Model):
    __tablename__ = 'orders'
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), autoincrement=True)
    date = db.Column(DateTime, default=datetime.utcnow)
    total_quantity = db.Column(db.Integer)
    total_price = db.Column(db.Float)
    items = relationship('Order_Items', back_populates="order")

class Order_Items(db.Model):
    __tablename__ = 'order_items'
    item_id = db.Column(db.Integer, db.ForeignKey('inventory.item_id'), primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id', ondelete='CASCADE'), primary_key=True, autoincrement=True)
    item_quantity = db.Column(db.Integer)
    item_total_price = db.Column(db.Float)
    order = relationship('Orders', back_populates="items")
    item = relationship('Inventory')

class Payments(db.Model):
    __tablename__ = 'payments'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id', ondelete='CASCADE'))
    name = db.Column(db.String(50))
    email = db.Column(db.String(150))
    address_one = db.Column(db.String(100))
    address_two = db.Column(db.String(50), nullable=True)
    country = db.Column(db.String(50))
    state = db.Column(db.String(50))
    zip_code = db.Column(db.Integer)
    name_on_card = db.Column(db.String(50))
    card_numbers = db.Column(db.String(16))
    expiration = db.Column(db.Integer)
    cvv = db.Column(db.Integer)

