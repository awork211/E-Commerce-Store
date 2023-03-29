from flask import Flask, render_template, request, url_for, redirect, session
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint
from flask_login import current_user

views = Blueprint('views', __name__, url_prefix='/')

@views.route('/')
def home():
    return render_template('index.html', user = current_user)

@views.route('products/<category>')
def products(category):
    return
    # add inventory query to check category, pass to template


@views.route('products/<category>/<item_id>')
def product_item(category, item_id):
    return item_id
    # query using item id
    # pass to item page template