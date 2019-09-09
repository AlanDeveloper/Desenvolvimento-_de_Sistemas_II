# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, redirect, session
from ..models.departamento import departamento
from .. import db
import hashlib

dep_bp = Blueprint('depto', __name__, url_prefix='/departamento', template_folder='templates')

@dep_bp.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        resp = departamento()
        resp.nome = request.form['nome']
        
        db.session.add(resp)
        db.session.commit()
        return redirect('/departamento/listar')
    else:
        return render_template('departamento/form.html')

@dep_bp.route('/listar', methods=['GET'])
def listar():
    lista = departamento.query.all()
    return render_template('departamento/list.html', lista=lista)

@dep_bp.route('/deletar/<id>', methods=['GET', 'POST'])
def deletar(id):
    departamento.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect('/departamento/listar')

@dep_bp.route('/atualizar/<id>', methods=['GET', 'POST'])
def atualizar(id):
    if request.method == 'POST':
        resp = departamento()
        resp.nome = request.form['nome']
        resp.id = id

        db.session.merge(resp)
        db.session.commit()
        return redirect('/departamento/listar')
    else:
        u = departamento.query.filter_by(id=id).first()
        return render_template('departamento/alt.html', u=u)