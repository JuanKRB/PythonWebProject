# . is import from the current package
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy.types import DateTime

class Estudiantes(db.Model, UserMixin):
    id_estudiante = db.Column(db.Integer, primary_key=True)
    contra = db.Column(db.String(355), unique=True)
    nombre = db.Column(db.String(60))
    correo = db.Column(db.String(70))
    id_idioma = db.Column(db.Integer)
    # id_idioma = db.Column(db.Integer, db.ForeignKey('idiomas.id_idioma'))

    def get_id(self):
        return self.id_estudiante

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

class Colaboradores(db.Model, UserMixin):
    __tablename__ = 'Colaboradores'
    id_colaborador = db.Column(db.Integer, primary_key=True)
    contra = db.Column(db.String(355), unique=True)
    nombre = db.Column(db.String(60))
    correo = db.Column(db.String(70))

    def get_id(self):
        return self.id_colaborador

class Idiomas(db.Model):
    __tablename__ = 'Idiomas'
    id_idioma = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(60))

    def get_id(self):
        return self.id_idioma

class Contenido(db.Model):
    __tablename__ = 'Contenido'
    id_contenido = db.Column(db.Integer, primary_key=True)
    id_idioma = db.Column(db.Integer, db.ForeignKey('Idiomas.id_idioma'), nullable=False)

    def get_id(self):
        return self.id_contenido

    @property
    def nombreIdioma(self):
        return self.setNombreIdioma(self.id_idioma)

    @staticmethod
    def setNombreIdioma(id_idioma):
        nombreIdioma = None
        if id_idioma == 1:
            nombreIdioma = "Español"
        elif id_idioma == 2:
            nombreIdioma = "Inglés"
        elif id_idioma == 3:
            nombreIdioma = "Francés"
        elif id_idioma == 4:
            nombreIdioma = "Alemán"
        elif id_idioma == 5:
            nombreIdioma = "Italiano"
        elif id_idioma == 6:
            nombreIdioma = "Portugués"
        elif id_idioma == 7:
            nombreIdioma = "Mandarín"
        elif id_idioma == 8:
            nombreIdioma = "Japonés"
        elif id_idioma == 9:
            nombreIdioma = "Coreano"
        elif id_idioma == 10:
            nombreIdioma = "Ruso"

        return nombreIdioma

class Teoria(db.Model):
    __tablename__ = 'Teoria'
    id_teoria = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(70))
    descripcion = db.Column(db.String(70))
    fecha = db.Column (db.DateTime(timezone=True), default=func.now())
    texto = db.Column(db.String(300))

    def get_id(self):
        return self.id_teoria

class Multimedia(db.Model):
    __tablename__ = 'Multimedia'
    id_multimedia = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(70))
    descripcion = db.Column(db.String(70))
    fecha = db.Column (db.DateTime(timezone=True), default=func.now())
    url = db.Column(db.String(150))

    def get_id(self):
        return self.id_multimedia

class Complete(db.Model):
    __tablename__ = 'Complete'
    id_complete = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(70))
    descripcion = db.Column(db.String(70))
    fecha = db.Column (db.DateTime(timezone=True), default=func.now())
    texto = db.Column(db.String(80))
    respuesta = db.Column(db.String(80))

    def get_id(self):
        return self.id_complete

class SeleccionMultiple(db.Model):
    __tablename__ = 'SeleccionMultiple'
    id_seleccionMultiple = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(70))
    descripcion = db.Column(db.String(70))
    fecha = db.Column (db.DateTime(timezone=True), default=func.now())
    texto = db.Column(db.String(80))
    respuestaCorrecta = db.Column(db.String(80))
    respuesta2 = db.Column(db.String(80))
    respuesta3 = db.Column(db.String(80))

    def get_id(self):
        return self.id_seleccionMultiple

class Asocie(db.Model):
    __tablename__ = 'Asocie'
    id_asocie = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(70))
    descripcion = db.Column(db.String(70))
    fecha = db.Column (db.DateTime(timezone=True), default=func.now())
    texto1 = db.Column(db.String(80))
    respuesta1 = db.Column(db.String(80))
    texto2 = db.Column(db.String(80))
    respuesta2 = db.Column(db.String(80))
    texto3 = db.Column(db.String(80))
    respuesta3 = db.Column(db.String(80))

    def get_id(self):
        return self.id_asocie

class VersionContenido(db.Model):
    __tablename__ = 'versioncontenido'
    id_version = db.Column(db.Integer, primary_key=True)
    id_complete = db.Column(db.Integer, db.ForeignKey('Complete.id_complete'))
    id_seleccionMultiple = db.Column(db.Integer, db.ForeignKey('SeleccionMultiple.id_seleccionMultiple'))
    id_teoria = db.Column(db.Integer, db.ForeignKey('Teoria.id_teoria'))
    id_asocie = db.Column(db.Integer, db.ForeignKey('Asocie.id_asocie'))
    id_multimedia = db.Column(db.Integer, db.ForeignKey('Multimedia.id_multimedia'))
    estado = db.Column(db.String(2))
    es_version_principal = db.Column(db.Boolean)
    id_colaborador = db.Column(db.Integer, db.ForeignKey('Colaboradores.id_colaborador'), nullable=False)
    id_contenido = db.Column(db.Integer, db.ForeignKey('Contenido.id_contenido'), nullable=False)

    complete = db.relationship('Complete', backref='versiones')
    seleccion_multiple = db.relationship('SeleccionMultiple', backref='versiones')
    teoria = db.relationship('Teoria', backref='versiones')
    asocie = db.relationship('Asocie', backref='versiones')
    multimedia = db.relationship('Multimedia', backref='versiones')
    colaborador = db.relationship('Colaboradores', backref='versiones')
    contenido = db.relationship('Contenido', backref='versiones')

    def get_id(self):
        return self.id_asocie




