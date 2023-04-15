from flask import Flask, render_template, request, url_for, redirect, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_
from flask import Blueprint
from flask_login import current_user
from .models import User, Inventory
from . import db

views = Blueprint('views', __name__, url_prefix='/')

@views.route('/')
def home():
    return render_template('index.html', user = current_user)


@views.route('products/<category>')
def products(category):
    list_products = Inventory.query.filter_by(category=category)
    return render_template('products.html', products = list_products, user = current_user, tag = item_nametag)
    


@views.route('products/<category>/<item_id>')
def product_item(category, item_id):
    get_item = Inventory.query.filter_by(item_id = item_id).first()

    # get related products excluding current
    related_products = Inventory.query.filter(and_(Inventory.category == category, Inventory.item_id != item_id)).limit(4).all()

    return render_template('item.html',user = current_user, item = get_item, tag = item_nametag, related_products = related_products)


item_nametag = {
    "candles":  '- Soy Candle',
    "diffusers": 'Reed Diffuser',
    "soaps": 'Hand & Body Soap'
}