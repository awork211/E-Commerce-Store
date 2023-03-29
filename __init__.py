from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.secret_key = 'AJNCKSM MASDKCM'

    from .views import views
    from .auth import auth
    from .models import User, Inventory

    with app.app_context():
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://aaronwork:gamecube@localhost/postgres'
        db.init_app(app)
        db.create_all()

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    # load user id into login_manager
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    app.register_blueprint(views)
    app.register_blueprint(auth)

    return app
