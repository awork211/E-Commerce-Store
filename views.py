from flask import Flask, render_template, request, url_for, redirect, session
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint

views = Blueprint('views', __name__, url_prefix='/')

@views.route('/')
def home():
    return render_template('index.html')