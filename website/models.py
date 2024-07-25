# . is import from the current package
from . import db
from flask_login import UserMixin

class Estudiantes(db.Model, UserMixin):
    id_estudiante = db.Column(db.Integer, primary_key=True)
    contra = db.Column(db.String(355), unique=True)
    nombre = db.Column(db.String(60))
    correo = db.Column(db.String(70))
    id_idioma = db.Column(db.Integer)
    # id_idioma = db.Column(db.Integer, db.ForeignKey('idiomas.id_idioma'))

    def get_id(self):
        return self.id_estudiante

class Colaboradores(db.Model, UserMixin):
    id_colaborador = db.Column(db.Integer, primary_key=True)
    contra = db.Column(db.String(355), unique=True)
    nombre = db.Column(db.String(60))
    correo = db.Column(db.String(70))

    def get_id(self):
        return self.id_colaborador


class Administradores(db.Model, UserMixin):
    id_administrador = db.Column(db.Integer, primary_key=True)
    contra = db.Column(db.String(355), unique=True)
    nombre = db.Column(db.String(60))
    correo = db.Column(db.String(70))

    def get_id(self):
        return self.id_administrador

class SuperAdministradores(db.Model, UserMixin):
    id_super_administrador = db.Column(db.Integer, primary_key=True)
    contra = db.Column(db.String(355), unique=True)
    nombre = db.Column(db.String(60))
    correo = db.Column(db.String(70))

    def get_id(self):
        return self.id_super_administrador


