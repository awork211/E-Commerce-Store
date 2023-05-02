import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.secret_key = 'AJNCKSM MASDKCM'

    from .views import views
    from .auth import auth
    from .models import User

    with app.app_context():
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
        db.init_app(app)
        db.create_all()

        from .populate_inventory import check_and_populate_inventory
        check_and_populate_inventory()

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_message = 'Please try logging in.'
    login_manager.login_view = 'auth.login'

    # load user id into login_manager
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    app.register_blueprint(views)
    app.register_blueprint(auth)

    return app
