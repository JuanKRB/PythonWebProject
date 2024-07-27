from flask import Blueprint, render_template, session
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
def home():
    userType = session.get('userType', 'No definido')
    return render_template("home.html", user=current_user, userType=userType)

@views.route('/student')
@login_required
def student():
    userType = session.get('userType', 'No definido')
    return render_template("studentSession.html", user=current_user, userType=userType)

@views.route('/collaborator')
@login_required
def collaborator():
    userType = session.get('userType', 'No definido')
    return render_template("collaboratorSession.html", user=current_user, userType=userType)

@views.route('/admin')
@login_required
def admin():
    userType = session.get('userType', 'No definido')
    return render_template("admin.html", user=current_user, userType=userType)

@views.route('/superAdmin')
@login_required
def superAdmin():
    userType = session.get('userType', 'No definido')
    return render_template("superAdmin.html", user=current_user, userType=userType)

@views.route('/contenido')
def contenido():
    userType = session.get('userType', 'No definido')
    return render_template("generalContent.html", user=current_user, userType=userType)