from .. import db
from sqlalchemy import Column, Integer, String, ForeignKey

class usuario(db.Model):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    email = Column(String(100), unique=True)
    senha = Column(String(1000))
    idDepto = Column(Integer, ForeignKey('departamento.id', onupdate="CASCADE", ondelete="CASCADE"), nullable=True)
