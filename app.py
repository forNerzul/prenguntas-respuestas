from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

# aca instanciamos la base de datos con la configuracion de la app
db = SQLAlchemy(app)

class Categoria(db.Model):
    __tablename__ = 'categorias'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    preguntas = db.relationship('Pregunta', backref='categoria', lazy=True)

class Pregunta(db.Model):
    __tablename__ = 'preguntas'
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(200))
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'))
    respuestas = db.relationship('Respuesta', backref='pregunta', lazy=True)

class Respuesta(db.Model):
    __tablename__ = 'respuestas'
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(200))
    correcta = db.Column(db.Boolean)
    pregunta_id = db.Column(db.Integer, db.ForeignKey('preguntas.id'))



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/preguntas')
def preguntas():
    return render_template('preguntas.html')

with app.app_context(): # esto es para que se cree la base de datos con el contexto de la app
    db.create_all() # esto crea la base de datos