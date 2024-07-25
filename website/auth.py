from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from .models import Estudiantes, Colaboradores, Administradores, SuperAdministradores
from werkzeug.security import generate_password_hash, check_password_hash
from . import db ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        type = request.form.get('type')

        form_data = request.form
        print(form_data)

        if type == 'signUp':
            nameSingUp = request.form.get('nameSingUp')
            emailSingUp = request.form.get('emailSingUp')
            password1SingUp = request.form.get('password1SingUp')
            password2SingUp = request.form.get('password2SingUp')
            id_language = request.form.get('idioma')
            click = request.form.get('click')

            student = Estudiantes.query.filter_by(correo=emailSingUp).first()
            collaborator = Colaboradores.query.filter_by(correo=emailSingUp).first()
            administrator = Administradores.query.filter_by(correo=emailSingUp).first()
            super_administrator = SuperAdministradores.query.filter_by(correo=emailSingUp).first()

            if student or collaborator or administrator or super_administrator:
                flash("Correo ya en uso", category='error')
                return render_template("login.html", user=current_user, is_singUP=True)
            elif len(emailSingUp) < 4:
                flash("El email debe ser de 4 caracteres o mas", category='error')
                return render_template("login.html", user=current_user, is_singUP=True)
            elif len(nameSingUp) < 2:
                flash("El nombre debe ser de 2 caracteres o mas", category='error')
                return render_template("login.html", user=current_user, is_singUP=True)
            elif password1SingUp != password2SingUp:
                flash("Las contraseñas no son iguales", category='error')
                return render_template("login.html", user=current_user, is_singUP=True)
            elif len(password1SingUp) < 7:
                flash("La contraseña debe ser de 7 caracteres o mas", category='error')
                return render_template("login.html", user=current_user, is_singUP=True)
            else:
                if click:
                    new_collaborator = Colaboradores(contra=generate_password_hash(password1SingUp, method='pbkdf2:sha256'),
                                              nombre=nameSingUp, correo=emailSingUp)
                    db.session.add(new_collaborator)
                    db.session.commit()
                    login_user(new_collaborator, remember=True)
                    flash("Colaborador creado", category='success')
                    return redirect(url_for('views.collaborator'))
                else:
                    new_student = Estudiantes(contra=generate_password_hash(password1SingUp, method='pbkdf2:sha256'),
                                              nombre=nameSingUp, correo=emailSingUp, id_idioma=id_language)
                    db.session.add(new_student)
                    db.session.commit()
                    login_user(new_student, remember=True)
                    flash("Estudiante creado", category='success')
                    return redirect(url_for('views.student'))

        else:
            email= request.form.get('email')
            password = request.form.get('password')

            student = Estudiantes.query.filter_by(correo=email).first()
            collaborator = Colaboradores.query.filter_by(correo=email).first()
            administrator = Administradores.query.filter_by(correo=email).first()
            super_administrator = SuperAdministradores.query.filter_by(correo=email).first()

            if student:
                if check_password_hash(student.contra, password):
                    session['userType'] = 'E'
                    flash("Logueado Correctamente", category='success')
                    login_user(student, remember=True)
                    userType = session.get('userType', 'No definido')
                    return render_template('studentSession.html', user=current_user, userType=userType)

                else:
                    flash("Contraseña Incorrecta", category='error')
            elif collaborator:
                if check_password_hash(collaborator.contra, password):
                    session['userType'] = 'C'
                    flash("Logueado Correctamente", category='success')
                    login_user(collaborator, remember=True)
                    userType = session.get('userType', 'No definido')
                    return render_template('collaboratorSession.html', user=current_user, userType=userType)
                else:
                    flash("Contraseña Incorrecta", category='error')
            elif administrator:
                if check_password_hash(administrator.contra, password):
                    session['userType'] = 'A'
                    flash("Logueado Correctamente", category='success')
                    login_user(administrator, remember=True)
                    userType = session.get('userType', 'No definido')
                    return render_template('admin.html', user=current_user, userType=userType)
                else:
                    flash("Contraseña Admin Incorrecta", category='error')
            elif super_administrator:
                if check_password_hash(super_administrator.contra, password):
                    session['userType'] = 'SP'
                    flash("Logueado Correctamente", category='success')
                    login_user(super_administrator, remember=True)
                    userType = session.get('userType', 'No definido')
                    return render_template('superAdmin.html', user=current_user, userType=userType)
                else:
                    flash("Contraseña Admin Incorrecta", category='error')
            else:
                flash("Correo no existente", category='error')


    data = request.form
    print(data)
    userType = session.get('userType', 'No definido')
    return render_template("login.html", user=current_user, user2="Juan", boolean = False, userType=userType)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up')
def sign_up():
    return "<p>Sign Up</p>"


