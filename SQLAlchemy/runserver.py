#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from .app import app
from flask import redirect, session
# BluePrints
from flask import Blueprint
from .app.controllers.usuario import home_bp

# SQL Alchemy
from .app import db

uri = 'postgresql://postgres:postgres@localhost:5432/banco'
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY']="chave"
db.init_app(app)

app.register_blueprint(home_bp)

@app.before_first_request
def before():
    db.create_all()
    session['logged_in'] = False

@app.route('/')
def index():
    return redirect(home_bp.url_prefix)

@app.route('/usuario/cadastrar')
def cadastrar():
    return redirect(home_bp.url_prefix)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run('0.0.0.0', port=port)


