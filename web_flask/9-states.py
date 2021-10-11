#!/usr/bin/python3
"""Starts a Flask web application with the rutes /states and /states/<id>"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """Remove the current SQLAlchemy session"""
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """Displays an HTML page with a list of all the states or
     a specific state if an id is given"""
    if id:
        states = storage.all(State)
        state_id = "State.{}".format(id)
        if state_id in states:
            states = states[state_id]
        else:
            states = None
    else:
        states = storage.all(State).values()
    return(render_template('9-states.html', states=states, id=id))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
