#!/usr/bin/env python3
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app():
    """
    A function that creates the instance of the flask class

    Returns
    -------
    app :
        instance of the created flask class
    """
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # Deactivate auto sort for json keys
    app.json.sort_keys = False
    return (app)

app = create_app()
db = SQLAlchemy(app)
