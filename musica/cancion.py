from flask import Blueprint, render_template
from . import db

bp = Blueprint('cancion', __name__, url_prefix='/cancion')

@bp.route('/')
def canciones():
    consulta = """
        SELECT Name, TrackId FROM tracks
    """
    con = db.get_db()
    res = con.execute(consulta)
    lista_canciones = res.fetchall()
    pagina = render_template('Canciones.html',
                             canciones=lista_canciones)
    return pagina

@bp.route('/<int:id>')
def detalle(id):
    con = db.get_db()
    consulta1 = """
        SELECT Name FROM tracks WHERE TrackId = ?
    """  
    consulta2 = """
        SELECT a.Name AS Nombre, a.ArtistId AS ID FROM artists a JOIN albums al
        ON a.ArtistId = al.ArtistId JOIN tracks t
        ON al.AlbumId = t.AlbumId
        WHERE TrackId = ?
    """
    res = con.execute(consulta1, (id,))
    cancion = res.fetchone()
    res = con.execute(consulta2, (id, ))
    lista_artistas = res.fetchall()
    pagina = render_template('detalleCanciones.html', 
                             cancion=cancion, 
                             artistas=lista_artistas)

    return pagina 