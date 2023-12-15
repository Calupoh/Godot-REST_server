import sqlite3
import click
from flask import current_app, g


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

        return g.db


def close_db():
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    # Inicia la base en blanco y agrega la clave "admin", 
    # para registrar primer usuario
    db = get_db()

    with current_app.open_resource('esquema.sql') as f:
        db.executescript(f.read().decode('utf8'))
        db.execute('INSERT INTO invitacion VALUES ("admin")')


def add_user(user = str, psswd = str):
    # Aqui de sergregaran las claves que mas tarde se usaran para registrarse
    db = get_db()
    n_user = (user, psswd)
    db.execute('INSERT INTO use VALUES (?, ?)', n_user)


@click.command('init-db')
def init_db_command():
    """Limpiar base de datos y crear nuevas tablas."""
    init_db()
    click.echo('Initialized the database.')


@click.command('agregar-usuario')
@click.option(
    '--usuario', help='Agrega un usuario', prompt='usario: '
    '--password', help='Agrega contraseña del usuario', prompt='passwd: '
)
def add_invitacion_command(usuario = None, password = None):
    if usuario == None or password == None:
        click.echo('Falta usuario o contraseña')
    add_user(usuario, password)
    click.echo(f'Se a agregado el usuario {usuario}')

