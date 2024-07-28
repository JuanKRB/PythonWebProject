from website import create_app, db
from website.models import VersionContenido, Complete, SeleccionMultiple, Teoria, Asocie, Multimedia, Colaboradores, Contenido

app = create_app()

with app.app_context():
    versiones = VersionContenido.query.all()
    print("VersionContenido:", versiones)


if __name__ == '__main__':
    app.run(debug=True)

