#!/usr/bin/python3
"""
Starts a Flask web application for the AirBnB project
"""


from models import storage
from models.state import State
from models.city import City
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def appcontext_teardown(exc):
    """
    Removes current SQLAlchemy session
    """
    storage.close()


@app.route('/states', strict_slashes=False)
def state_information():
    """
    Displays a HTML page inside the BODY tag
    """
    return (render_template('9-states.html', states=storage.all(State)))


@app.route('/states/<string:id>', strict_slashes=False)
def state_id(id=None):
    """
    Displays a HTML page inside the BODY tag
    """
    for state in storage.all('State').values():
        if state.id == id:
            return (render_template('9-states.html', state = state))
        return (render_template('9-states.html'))

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
