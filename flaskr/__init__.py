import os
from flask import Flask

def create_app(add_config=None):
    # Crear app y configuracion
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if add_config is None:
        # cargar configuraciones adicionales a la instancia
        app.config.from_pyfile('config.py', silent=True)
    else:
	    # cargado configuraciones de prueba
        app.config.from_mapping(add_config)
    
    # asegurando la existencia de la carpeta instancia
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # Registrando Apps
    
    @app.route('/hola')
    def hola():
         return 'hola mundo'
        
    # ~ from . import gestor_db
    # ~ gestor_db.init_app(app)

    return app
