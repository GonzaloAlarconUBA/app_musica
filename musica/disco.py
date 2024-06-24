from flask import Blueprint, render_template
from . import db

bp = Blueprint('disco', __name__, url_prefix='/disco')

@bp.route('/')
def discos():
    consulta = """
        SELECT Title , AlbumId AS aId FROM albums
    """

    con = db.get_db()
    res = con.execute(consulta)
    lista_discos = res.fetchall()
    pagina = render_template('Discos.html',
                             discos=lista_discos)
    return pagina

@bp.route('/<int:id>')
def detalle(id):
    con = db.get_db()
    consulta1 = """
        SELECT Title, AlbumId AS aId FROM albums WHERE AlbumId = ?
    """  
    consulta2 = """
        SELECT Name, TrackId, a.AlbumId AS aId FROM albums a JOIN tracks t  
        ON a.AlbumId = t.AlbumId 
        WHERE a.AlbumId = ?
    """
    res = con.execute(consulta1, (id,))
    disco = res.fetchone()
    res = con.execute(consulta2, (id, ))
    lista_canciones = res.fetchall()
    pagina = render_template('detalleDiscos.html', 
                             disco=disco, 
                             canciones=lista_canciones)

    return pagina 