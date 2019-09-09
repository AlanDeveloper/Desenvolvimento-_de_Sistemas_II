from .. import db
from sqlalchemy import Column, Integer, String, DateTime

class departamento(db.Model):
    __tablename__ = 'departamento'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    data_atualizacao = db.Column(db.DateTime, unique=True, default=db.func.now())