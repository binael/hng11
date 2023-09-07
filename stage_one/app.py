#!/usr/bin/env python3

"""
Flask module
"""

from flask import Flask, request, jsonify
from dict_generator import dict_gen as gen

# Create flask app
app = Flask(__name__)
app.json.sort_keys = False

@app.route("/api", methods=["GET"], strict_slashes=False)
def home():
    """
    Returns api endpoint for hng11 project
    """
    name = request.args.get("slack_name")
    track = request.args.get("track")

    if name and track:
        return jsonify(gen(name, track))
    else:
        return None


if __name__ == "__main__":
    app.run(debug=True, port=5000)
