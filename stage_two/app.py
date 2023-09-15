#!/usr/bin/env python3

"""
Module containing api routes to implement CRUD operations on
a database

CRUD - CREATE READ UPDATE DELETE
"""

# Python modules
from flask import request
from flask import jsonify

# Imports from __init__.py
from extensions import app
from extensions import db

# Imports from model
from model import User

def create_tables():
    with app.app_context():
        db.create_all()

# # Import from dict_converter
from dict_converter import class2dict
from dict_converter import multi_class2dict


@app.route('/api', methods=['POST'], strict_slashes=False)
def create_new_object():
    """
    Function that creates a new object or row in a database
    """
    user_id = request.json.get('user_id')
    name = request.json.get('name')
    if user_id and name:
        #Check if user_id is int else fail
        if not isinstance(user_id, int):
            return ('', 500)
        # If id already exists, assign new id, else create with the id
        user = User.query.filter_by(user_id=user_id).first()
        if not user:
            user = User(user_id=user_id, name=name.split(';')[0])
    if name:
        name = name.split(';')[0]
        user = User(name=name)
        db.session.add(user)
        db.session.commit()
        return ('', 204)
    else:
        return ('FAILED', 500)



@app.route('/api', methods=['GET'], strict_slashes=False)
def retrieve_all():
    """
    Gets all the details of data in the database
    """
    users = User.query.all()
    if users:
        return jsonify(multi_class2dict(users))
    else:
        return ('', 404)


@app.route('/api/<int:id>', methods=['GET'], strict_slashes=False)
def retrieve_id(id):
    """
    Gets only the detail of the specified id
    """
    user = User.query.filter_by(user_id=id).first()
    if user:
        return jsonify(class2dict(user))
    else:
        return ('', 404)


@app.route('/api/<int:id>', methods=['PUT'], strict_slashes=False)
def update(id):
    """
    Function that updates database objects
    """
    user = User.query.filter_by(user_id=id).first()
    name = request.json.get('name')
    if user and name:
        name = name.split(';')[0]
        # Delete the previous user
        db.session.delete(user)
        db.session.commit()
        # Assign the same id as the previous user
        user_id = id
        # Create new user and commit
        new_user = User(user_id=id, name=name)
        db.session.add(new_user)
        db.session.commit()
        return ('', 204)
    else:
        return ('FAILED', 500)


@app.route('/api/<int:id>', methods=['DELETE'], strict_slashes=False)
def delete_id(id):
    """
    Function that deletes object in the database
    """
    user = User.query.filter_by(user_id=id).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return ('', 204)
    else:
        return ('NO ID FOUND', 500)


if __name__ == '__main__':
    create_tables()
    app.run(debug=False, port=5000)
