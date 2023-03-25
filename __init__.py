from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.secret_key = 'AJNCKSM MASDKCM'

    from .views import views
    from .auth import auth
    from .models import User

    with app.app_context():
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://aaronwork:gamecube@localhost/postgres'
        db.init_app(app)
        db.create_all()

    app.register_blueprint(views)
    app.register_blueprint(auth)

    return app
