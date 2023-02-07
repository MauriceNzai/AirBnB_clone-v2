#!/usr/bin/python3
"""
Starts a Flask web application 
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
@app.route('/states/<id>', strict_slashes=False)
def state_city_info():
    """
    Displays a HTML page inside the BODY tag
    """
    states = storage.all(State)

    if not id:
        html_dict = {value.id: value.name for value in states.values()}
        return (render_template(
            '7-states_list.html', Table='States', items=html_dict))
    key = 'State.{}'.format(id)
    if key in states:
        return (render_template(
            '9-states.html', Table='State: {}'.format(
                states[key].name),items=states[key]))
    return (render_template('9-states.html', items=None))        

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
