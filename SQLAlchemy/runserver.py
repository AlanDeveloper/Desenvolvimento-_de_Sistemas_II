#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from .app import app
from flask import redirect, session
# BluePrints
from flask import Blueprint, render_template
from .app.controllers.usuario import home_bp
from .app.controllers.departamento import dep_bp

# SQL Alchemy
from .app import db

uri = 'postgresql://postgres:postgres@localhost:5432/banco'
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY']="chave"
db.init_app(app)

app.register_blueprint(home_bp)
app.register_blueprint(dep_bp)

@app.before_first_request
def before():
    db.create_all()
    session['logged_in'] = False

@app.route('/')
def home():
    return render_template('base.html')