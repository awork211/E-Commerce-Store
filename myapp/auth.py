from flask import Flask, render_template, request, url_for, redirect, session, flash, Blueprint
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db

auth = Blueprint('auth', __name__, url_prefix='/')

@auth.route("signup", methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        user_email = request.form['email']
        first_name = request.form['firstName']
        password = request.form['password']

        # query for user data
        if db.session.query(User).filter(User.email == user_email).count() != 0:
            flash('An account exists with this email.', category='error')
        else:
            new_user = User(email = user_email, password = generate_password_hash(password, method='sha256'),
            first_name = first_name)
            
            db.session.add(new_user)
            db.session.commit()

            user = User.query.filter_by(email=user_email).first()
            login_user(user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))
    return render_template('signup.html', user = current_user)

@auth.route("login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully!", category="success")
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Incorrect password, please try again.", category="error")
        else:
            flash("Email does not exist.", 'error')
    return render_template('login.html', user = current_user)

@auth.route("logout", methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))