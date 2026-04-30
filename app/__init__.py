#!/usr/bin/env python3

from flask import Flask
from .models import db

def create_app(config_name=None):
    app = Flask(__name__)

    if config_name == "TestingConfig":
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testing.db'
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    return app
