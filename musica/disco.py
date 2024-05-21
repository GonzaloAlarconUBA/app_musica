from flask import Blueprint, render_template
from . import db


bp = Blueprint('disco', __name__, url_prefix='/disco')

@bp.route('/')
def discos():
    consulta = """
        SELECT Title FROM albums
    """

    con = db.get_db()
    res = con.execute(consulta)
    lista_discos = res.fetchall()
    pagina = render_template('Discos.html',
                             discos=lista_discos)
    return pagina
