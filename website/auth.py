from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Estudiantes
from werkzeug.security import generate_password_hash, check_password_hash
from . import db ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        type = request.form.get('type')
        if type == 'signUp':
            nameSingUp = request.form.get('nameSingUp')
            emailSingUp = request.form.get('emailSingUp')
            password1SingUp = request.form.get('password1SingUp')
            password2SingUp = request.form.get('password2SingUp')
            id_language = request.form.get('idioma')

            student = Estudiantes.query.filter_by(correo=emailSingUp).first()
            if student:
                flash("Correo ya en uso", category='error')
            elif len(emailSingUp) < 4:
                flash("El email debe ser de 4 caracteres o mas", category='error')
            elif len(nameSingUp) < 2:
                flash("El nombre debe ser de 2 caracteres o mas", category='error')
            elif password1SingUp != password2SingUp:
                flash("Las contraseñas no son iguales", category='error')
            elif len(password1SingUp) < 7:
                flash("La contraseña debe ser de 7 caracteres o mas", category='error')
            else:
                new_student = Estudiantes(contra=generate_password_hash(password1SingUp, method='pbkdf2:sha256'), nombre=nameSingUp, correo=emailSingUp,id_idioma=id_language)
                db.session.add(new_student)
                db.session.commit()
                login_user(student, remember=True)
                flash("Cuenta creada", category='success')
                return redirect(url_for('views.student'))
        else:
            email= request.form.get('email')
            password = request.form.get('password')

            student = Estudiantes.query.filter_by(correo=email).first()
            if student:
                if check_password_hash(student.contra, password):
                    flash("Logueado Correctamente", category='success')
                    login_user(student, remember=True)
                    return redirect(url_for('views.student'))
                else:
                    flash("Contraseña Incorrecta", category='error')
            else:
                flash("Correo no existente", category='error')


    data = request.form
    print(data)
    return render_template("login.html", user="Juan", boolean = False)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up')
def sign_up():
    return "<p>Sign Up</p>"


