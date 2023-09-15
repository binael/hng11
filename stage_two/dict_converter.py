#!/usr/bin/env python3

"""
A module that converts lists db row objects into dict for
json conversion
"""

def class2dict(user_list) -> dict:
    """
    Function that converts a single db object (row)
    into dictionary

    Parameters
    ----------
    user_list : list
        A list containing row database objects

    Returns
    -------
    dict :
        Dictionary for object row
    """
    my_dict = {
        'user_id': user_list.user_id,
        'name': user_list.name
	}
    return (my_dict)


def multi_class2dict(user_list) -> list:
    """
    Function that converts a single db objects (rows)
    into list of dictionaries

    Parameters
    ----------
    user_list : list
        A list containing row database objects

    Returns
    -------
    list :
        A list of dictionaries
    """
    new_list = []
    for user in user_list:
        my_dict = {
            'user_id': user.user_id,
            'name': user.name
		}
        new_list.append(my_dict)
    return (new_list)
