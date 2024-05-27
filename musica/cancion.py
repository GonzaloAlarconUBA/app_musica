from flask import Blueprint, render_template
from . import db

bp = Blueprint('cancion', __name__, url_prefix='/cancion')

bp.route('/')
def canciones():
    consulta = """
        SELECT Name FROM tracks
    """
    con = db.get_db()
    res = con.execute(consulta)
    lista_canciones = res.fetchall()
    pagina = render_template('Canciones.html',canciones=lista_canciones)
    return pagina