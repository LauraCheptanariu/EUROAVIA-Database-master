"""
1. Fisierul auth.py - cuprinde toate paginile ce tin de login/logout
2. Aveti mai jos exemplu de pagina - login
3. Pagini ce trebuie implementate:
    - login
    - logout
    - sign-up

* recomand sa va uitati la link ul de la pct 7 de pe main
"""

from flask import Blueprint, render_template, request, flash, redirect, url_for
import models
from werkzeug.security import generate_password_hash, check_password_hash
from models import db
from flask_login import login_user, login_required, logout_user , current_user


auth = Blueprint('auth', __name__)

@auth.route('/login', methodes=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        person= Person.query.filter_by(email=email).first()
        if person:
            if check_password_hash(Person.password, password):
                flash('Logged in succesfully', category='succes')
                login_user(person, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist' , category= 'error')

    return render_template("login.html", user=current_user) # aici se face conexiunea cu front-end-ul


@auth.route('/log_out', methods = ['GET', 'POST'])
@login_required

def log_out():

    logout_user()

    return render_template("log_out.html")


@auth.route('/sign_up', methods = ['GET', 'POST'])
def sign_up():

    if request.method == 'POST':
        email = request.form.get('email')
        first_name= request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        type = request.form.get('type')

        admin= Admin.query.filter_by(email=email).first()
        if admin:
            flash('Email already exists', category='error')
        elif email[-22] == '@euroavia-bucuresti.ro':
            flash('You need an Euroavia Bucuresti email.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:   
            new_admin = Admin( email=email, first_name=first_name, password=generate_password_hash(password1 , method='sha256'), type=type)
            db.session.add(new_admin)
            db.session.comit
            
    return render_template("sign_up.html")