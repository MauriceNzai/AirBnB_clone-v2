#!/usr/bin/python3
"""
Display a Flask web application for the AirBnB project
"""

from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template

app = Falsk(__name__)

@app.teardown_appcontext
def appcontext_teardown(self):
    """
    Fetches data for the storage engine using storage
    """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def state_id():
    """
    Displays a HTML page in the BODY tag
    """
    return (render_template('10-hbnb_filters.html', states=storage.all(State),
            amenities=storage.all(Amenity)))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
