#!/usr/bin/python3
"""Starts a Flask application and display Hello HBNB!"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello_HBNB():
    """Displays Hello HBNB!"""
    return("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """Displays HBNB"""
    return("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun():
    """Displays C followed by the value of text"""
    return("c {}".format(text.replace('_', ' ')))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
