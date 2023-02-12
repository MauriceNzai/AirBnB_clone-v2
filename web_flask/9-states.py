#!/usr/bin/python3
"""
Starts a Flask web application for task 9
and checks the status of the app
"""
from models import storage
from models.state import State
from models.city import City
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def appcontext_teardown(self):
    """
    Removes current SQLAlchemy session
    """
    storage.close()


@app.route('/states', strict_slashes=False)
def state_info():
    """
    Display HTML Page inside Body tag
    """
    return (render_template('7-states_list.html', states=storage.all(State)))


@app.route('/states/<string:id>', strict_slashes=False)
def state_id(id=None):
    """
    Displays a HTML page inside the BODY tag
    """
    return (render_template('9-states.html', states=storage.all(State).get(
            'State.{}'.format(id))))

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
