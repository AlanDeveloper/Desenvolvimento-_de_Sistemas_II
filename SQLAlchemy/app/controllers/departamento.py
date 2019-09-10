# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, redirect, session
from ..models.departamento import departamento
from .. import db
import hashlib

dep_bp = Blueprint('depto', __name__, url_prefix='/departamento', template_folder='templates')

@dep_bp.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form['nome']
        resp = departamento(nome)
        
        departamento.adicionar(resp)
        return redirect('/departamento/listar')
    else:
        return render_template('departamento/form.html')

@dep_bp.route('/listar', methods=['GET'])
def listar():
    lista = departamento.listar()
    return render_template('departamento/list.html', lista=lista)

@dep_bp.route('/deletar/<id>', methods=['GET', 'POST'])
def deletar(id):
    departamento.deletar(id)
    return redirect('/departamento/listar')

@dep_bp.route('/atualizar/<id>', methods=['GET', 'POST'])
def atualizar(id):
    if request.method == 'POST':
        nome = request.form['nome']
        resp = departamento(nome)
        resp.id = id

        departamento.atualizar(resp)
        return redirect('/departamento/listar')
    else:
        u = departamento.buscar(id)
        return render_template('departamento/alt.html', u=u)