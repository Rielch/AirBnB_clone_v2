#!/usr/bin/python3
"""Starts a web application and displays a list of states"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """Removes the current SQLAlchemy session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays a list of states"""
    states = storage.all(State).values()
    return(render_template('7-states_list.html', states=states))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5004)
