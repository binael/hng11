#!/usr/bin/env python3

"""
A module that generates a dictionary for api data
"""

from datetime import datetime

def dict_gen(slack_name: str, track: str) -> dict:
    """
    A function that generates a dictionary for api end
    point

    Parameters
    ----------
    slack_name: str
        The slack username
    track: str
        The currect track in slack
        Values may be 'backend, frondend' etc

    Returns
    -------
    dict:
        A dictionary to be that will be jsonified and returned
    """

    utc_datetime = datetime.utcnow()
    date = utc_datetime.strftime("%Y-%m-%dT%H:%M:%SZ")
    weekday = utc_datetime.strftime("%A")

    new_dict = {
        "slack_name": slack_name,
        "current_day": weekday,
        "utc_time": date,
        "track": track,
        "github_file_url": "https://github.com/binael/hng11/blob/main/stage_one/app.py",
        "github_repo_url": "https://github.com/binael/hng11",
        "status_code": 200
	}

    return (new_dict)
