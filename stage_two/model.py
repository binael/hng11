#!/usr/bin/env python3

"""
A module that creates an object class for the db schema
"""

from extensions import db
from extensions import app


class User(db.Model):
    """
    A class that represents an table object in the database

    Parameters
    ----------
    tablename : str
        The name of the database table
    user_id : int
        The unique id for every user
    name : str
        The name of the the user
    """
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)

    # def __init__(self, user_id, name) -> None:
    #     """
    #     Instance variables
    #     """
    #     self.user_id = user_id
    #     self.name = name

    def __repr__(self):
        """
        String representation of the object
        """
        return f"User: id=<{self.user_id} name=<{self.name}>"
