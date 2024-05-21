from flask import Flask,render_template

app = Flask(__name__)

with app.app_context():
    from . import db
    db.init_app(app)

@app.route('/')
def hello():
    return 'Hello, World!'

from . import artista
app.register_blueprint(artista.bp)


@app.route('/cancion')
def canciones():
    consulta = """
        SELECT Name FROM tracks
    """
    con = db.get_db()
    res = con.execute(consulta)
    lista_canciones = res.fetchall()
    pagina = render_template('Canciones.html',canciones=lista_canciones)
    return pagina

