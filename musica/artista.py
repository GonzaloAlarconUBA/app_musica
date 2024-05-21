from flask import Blueprint, render_template
from . import db

bp = Blueprint('artista', __name__, url_prefix='/artista')

@bp.route('/')
def artistas():
    consulta = """
        SELECT Name, ArtistId FROM artists
    """

    con = db.get_db()
    res = con.execute(consulta)
    lista_artistas = res.fetchall()
    pagina = render_template('Artistas.html',artistas=lista_artistas)
    return pagina


@bp.route('/<int:id>')
def detalle(id):
    con = db.get_db()
    consulta1 = """
        SELECT Name FROM artists WHERE ArtistId = ?
    """  
    consulta2 = """
        SELECT Title, AlbumId FROM albums a JOIN artists ar  
        ON a.ArtistId = ar.ArtistId 
        WHERE a.ArtistId = ?
    """
    res = con.execute(consulta1, (id,))
    artista = res.fetchone()
    res = con.execute(consulta2, (id, ))
    lista_albums = res.fetchall()
    pagina = render_template('detalleArtista.html', 
                             artista=artista, 
                             albums=lista_albums)

    return pagina 