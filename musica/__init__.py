from flask import Flask,render_template

app = Flask(__name__)

with app.app_context():
    from . import db
    db.init_app(app)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/artistas')
def artistas():
    consulta = """
        SELECT Name FROM artists
    """

    con = db.get_db()
    res = con.execute(consulta)
    lista_artistas = res.fetchall()
    pagina = render_template('Artistas.html',artistas=lista_artistas)
    return pagina

@app.route('/canciones')
def canciones():
    consulta = """
        SELECT Name FROM tracks
    """

    con = db.get_db()
    res = con.execute(consulta)
    lista_canciones = res.fetchall()
    pagina = render_template('Canciones.html',canciones=lista_canciones)
    return pagina

@app.route('/discos')
def discos():
    consulta = """
        SELECT Title FROM albums
    """

    con = db.get_db()
    res = con.execute(consulta)
    lista_discos = res.fetchall()
    pagina = render_template('Discos.html',discos=lista_discos)
    return pagina