#!/usr/bin/python3
"""
Starts a Flask web application for the AirBnB project
"""


from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def appcontext_teardown(self):
    """
    Calls storage for fetching data from the storage engine
    """
    storage.close()


@app.route('/states', strict_slaashes=False)
def state_information():
    """
    Displays a HTML page inside the BODY tag
    """
    return (render_template('7-states_list.html', states=storage.all(State)))


@qpp.route('/states/<string:id>', strict_slashes=False)
def state_id(id=None):
    """
    Displays a HTML page inside the BODY tag
    """
    return (render_template('9-states.html', states=storage.all(State).get(
        'State.{}'.format(id))))


    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
