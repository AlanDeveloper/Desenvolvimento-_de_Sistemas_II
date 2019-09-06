# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, redirect
from ..models.usuario import usuario
from .. import db
import hashlib

home_bp = Blueprint('home', __name__, url_prefix='/usuario', template_folder='templates')

@home_bp.route('/')
def home():
    return render_template('usuario/home.html')

@home_bp.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        resp = usuario()
        resp.nome = request.form['nome']
        resp.email = request.form['email']
        resp.senha = request.form['senha']
        
        db.session.add(resp)
        db.session.commit()
        return redirect('/usuario/listar')
    else:
        return render_template('usuario/form.html')

@home_bp.route('/listar', methods=['GET'])
def listar():
    lista = usuario.query.all()
    return render_template('usuario/list.html', lista=lista)

@home_bp.route('/deletar/<id>', methods=['GET', 'POST'])
def deletar(id):
    usuario.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect('/usuario/listar')

@home_bp.route('/atualizar/<id>', methods=['GET', 'POST'])
def atualizar(id):
    if request.method == 'POST':
        resp = usuario()
        resp.nome = request.form['nome']
        resp.email = request.form['email']
        resp.senha = request.form['senha']
        resp.id = id

        db.session.merge(resp)
        db.session.commit()
        return redirect('/usuario/listar')
    else:
        u = usuario.query.filter_by(id=id).first()
        return render_template('usuario/alt.html', u=u)