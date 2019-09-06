# -*- coding: utf-8 -*-
__version__ = '0.1'
from flask import Flask
from .controllers import *
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__, template_folder="templates")