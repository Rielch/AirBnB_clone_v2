#!/usr/bin/python3
"""Displays an HBNB page with the popover for the filters"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """Remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def state():
    """Returns a list of all State objects"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return(render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5004)
