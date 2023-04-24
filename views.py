from flask import Flask, render_template, request, url_for, redirect, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_
from flask import Blueprint
from flask_login import current_user, login_required
from .models import User, Inventory, Orders, Order_Items, Payments
from . import db

views = Blueprint('views', __name__, url_prefix='/')

@views.route('/')
def home():
    return render_template('index.html', user = current_user)


@views.route('products/<category>')
def products(category):
    list_products = Inventory.query.filter_by(category=category)
    print(list_products)
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

@views.route('order_payment', methods=['POST'])
def order_payment():
    # Payment data
    customer_name = request.form['first_name'] + ' ' + request.form['last_name']
    email = request.form['email']
    address1 = request.form['address1']
    address2 = request.form['address2']
    country = request.form['country']
    state = request.form['state']
    zip_code = request.form['zip_code']
    name_on_card = request.form['name_on_card']
    card_numbers = request.form['card_numbers']
    expiration = request.form['expiration']
    cvv = request.form['cvv']

    # Order
    user_id = current_user.id
    order_total_quantity = session['cart_total_quantity']
    order_total_price = session['cart_total_price']

    new_order = Orders(user_id = user_id, total_quantity = order_total_quantity, total_price = order_total_price)

    db.session.add(new_order)
    db.session.commit()

    # Order Items
    last_order = Orders.query.filter_by(user_id=user_id).order_by(Orders.date.desc()).first()
    last_order_id = last_order = last_order.order_id
    for key, value in session['cart_item'].items():
        item_id = int(key)
        item_price = value['total_price']
        item_quantity = value['quantity']
        order_items = Order_Items(item_id = item_id, order_id = last_order_id, item_quantity = item_quantity, item_total_price = item_price)

        db.session.add(order_items)
        db.session.commit()


    # Payment
    payment_info = Payments(
        user_id = user_id,
        order_id = last_order_id,
        name = customer_name,
        email = email,
        address_one = address1,
        address_two = address2,
        country = country,
        state = state,
        zip_code = zip_code,
        name_on_card = name_on_card,
        card_numbers = card_numbers,
        expiration = expiration,
        cvv = cvv
    )
    db.session.add(payment_info)
    db.session.commit()

    return redirect(url_for('views.order_complete'))

@views.route('order_success', methods=['GET', 'POST'])
def order_complete():
    session.clear()
    return render_template('order_success.html', user = current_user)


item_nametag = {
    "candles":  '- Soy Candle',
    "diffusers": 'Reed Diffuser',
    "soaps": 'Soap Variety'
}