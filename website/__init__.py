from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_USER = 'root'
DB_PASSWORD = '1234'
DB_HOST = 'localhost'
DB_PORT = '3306'
DB_NAME = 'db_analisis'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '12ab'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import Estudiantes

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id_estudiante):
        return Estudiantes.query.get(int(id_estudiante))

    return app

def create_database(app):
    with app.app_context():
        db.create_all()
        print('Database created!')

