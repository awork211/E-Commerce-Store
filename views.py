from flask import Flask, render_template, request, url_for, redirect, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_
from flask import Blueprint
from flask_login import current_user, login_required
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

@views.route('cart')
def cart():
    return render_template('cart.html', user = current_user)

@views.route('add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        item_id = request.form['item_id']
        item_quantity = int(request.form['quantity'])

        get_item = Inventory.query.filter_by(item_id=item_id).first()

        price = float(get_item.price)

        item_dict = {item_id: {
            'name': get_item.item_name + ' ' + item_nametag[get_item.category],
            'item_id': item_id,
            'quantity': item_quantity,
            'price': price,
            'total_price': item_quantity * price
        }}

        cart_total_price = 0
        cart_total_quantity = 0

        if 'cart_item' in session:
            if item_id in session['cart_item']:
                old_quantity = session['cart_item'][item_id]['quantity']
                total_quantity = old_quantity + item_quantity
                session['cart_item'][item_id]['total_price'] = format(total_quantity * price, '.2f')
                session['cart_item'][item_id]['quantity'] = total_quantity
            else:
                session['cart_item'].update(item_dict)

            for key, value in session['cart_item'].items():
                individual_quantity = int(value['quantity'])
                individual_price = float(value['total_price'])
                cart_total_price += individual_price
                cart_total_quantity += individual_quantity
        else:
            session['cart_item'] = item_dict
            cart_total_price = price * item_quantity
            cart_total_quantity = item_quantity

        session['cart_total_price'] = format(cart_total_price, '.2f')
        session['cart_total_quantity'] = cart_total_quantity
        session.modified = True
    return redirect(request.referrer)



@views.route('delete_item/<item_id>')
def delete(item_id):
    print(item_id)
    cart_total_quantity = 0
    cart_total_price = 0

    for i in session['cart_item'].items():
        if i[0] == item_id:
            product = session['cart_item'].pop(i[0], None)
            print(product)
            if 'cart_item' in session:
                for key, value in session['cart_item'].items():
                    individual_quantity = int(session['cart_item'][key]['quantity'])
                    individual_price = float(session['cart_item'][key]['total_price'])
                    cart_total_quantity += individual_quantity
                    cart_total_price += individual_price
            break

    if cart_total_quantity == 0:
        session.clear()
    else:
        session['cart_total_quantity'] = cart_total_quantity
        session['cart_total_price'] = format(cart_total_price, '.2f')
    session.modified = True
    return redirect(request.referrer)

@views.route('order_success', methods=['GET', 'POST'])
def order_complete():
    # create order table, and order_items in models
    # enter in order in db, order_items in db
    # clear session/cart
    # return a thank you template
    return 'Thank you for your order!'


item_nametag = {
    "candles":  '- Soy Candle',
    "diffusers": 'Reed Diffuser',
    "soaps": 'Hand & Body Soap'
}