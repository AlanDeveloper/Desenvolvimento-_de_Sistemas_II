from .. import db
from sqlalchemy import Column, Integer, String, DateTime

class departamento(db.Model):
    __tablename__ = 'departamento'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    data_atualizacao = db.Column(db.DateTime, unique=True, default=db.func.now(), onupdate= db.func.now())

    def __init__(self, nome):
        self.nome = nome

    def adicionar(d):
        db.session.add(d)
        db.session.commit()

    def listar():
        return departamento.query.all()
    
    def deletar(id):
        departamento.query.filter_by(id=id).delete()
        db.session.commit()

    def atualizar(d):
        db.session.merge(d)
        db.session.commit()

    def buscar(id):
        return departamento.query.filter_by(id=id).first()
