from .. import db
from sqlalchemy import Column, Integer, String, ForeignKey

class usuario(db.Model):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    email = Column(String(100), unique=True)
    senha = Column(String(1000))
    idDepto = Column(Integer, ForeignKey('departamento.id', onupdate="CASCADE", ondelete="CASCADE"), nullable=True)

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def adicionar(u):
        db.session.add(u)
        db.session.commit()

    def listar():
        return usuario.query.all()
    
    def deletar(id):
        usuario.query.filter_by(id=id).delete()
        db.session.commit()

    def atualizar(u):
        db.session.merge(u)
        db.session.commit()

    def buscar(id):
        return usuario.query.filter_by(id=id).first()
    
    def entrar(email, senha):
        return usuario.query.filter_by(email=email, senha=senha).first()
