from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Empresa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    logo_url = db.Column(db.String(255))

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    foto_url = db.Column(db.String(255))

class Atividade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"))
    tipo = db.Column(db.String(20))
    distancia_m = db.Column(db.Integer)
    duracao_min = db.Column(db.Integer)
    calorias = db.Column(db.Integer)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)
    likes_count = db.Column(db.Integer, default=0)

    usuario = db.relationship("Usuario")
    comentarios = db.relationship("Comentario", backref="atividade")

class Comentario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    atividade_id = db.Column(db.Integer, db.ForeignKey("atividade.id"))
    texto = db.Column(db.String(255))
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)
