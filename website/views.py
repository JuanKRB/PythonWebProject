from flask import Blueprint, render_template, session, request
from .models import VersionContenido, Multimedia
from flask_login import login_required, current_user
from sqlalchemy.orm import joinedload

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

@views.route('/contenido', methods=['GET', 'POST'])
def contenido():
    if request.method == 'GET':
        try:
            versiones_contenido = VersionContenido.query.options(
                joinedload(VersionContenido.complete),
                joinedload(VersionContenido.seleccion_multiple),
                joinedload(VersionContenido.teoria),
                joinedload(VersionContenido.asocie),
                joinedload(VersionContenido.multimedia),
                joinedload(VersionContenido.colaborador),
                joinedload(VersionContenido.contenido)
            ).all()

            print("Versiones de contenido:", versiones_contenido)  # Verifica el contenido de la consulta

            userType = session.get('userType', 'No definido')
            return render_template('generalContent.html', versiones=versiones_contenido,
                                   user=current_user, userType=userType)
        except Exception as e:
            print(f"Error al obtener versiones de contenido: {e}")
            return str(e)

@views.route('/multimedia', methods=['GET', 'POST'])
def multimedia():
    userType = session.get('userType', 'No definido')
    id_multimedia = request.form.get('id_multimedia')

    multimedia = Multimedia.query.get(id_multimedia)

    return render_template("multimedia.html", user=current_user, userType=userType, multimedia=multimedia)





