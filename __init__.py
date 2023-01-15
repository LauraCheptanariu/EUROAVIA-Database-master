"""
1. Fisierul __init__.py al programului - aici se creaza efectiv web app-ul si baza de date
2. De modificat: 
    - trebuie sa agaugam partea de flask_login (pentru partea de admin)-> folositi Documentatia Flask
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "baza.db"

def create_app():
    """
    Functie ce creaza efectiv webapp-ul (la nivel local) si il conecteaza cu baza de date
    """

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'un_cod_irelevant_la_nivelul_la_care_lucram'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from views import views
    from auth import auth


    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.person_loader
    def load_person(id):
        return Person.query.get(int(id))

    return app

def create_database(app):
    """
    Funcite ce verifica daca baza de date exista. Daca nu exista, o creaza.
    """
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')