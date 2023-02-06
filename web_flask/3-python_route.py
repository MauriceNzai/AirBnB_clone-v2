#!/usr/bin/python3
"""
Starts a Flask Web Application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Starts a basic Flask web application
    """
    return ("Hello HBNB!")

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Adds the route /hbnb
    """
    return ("HBNB")

@app.route('/c/<string:text>', strict_slashes=False)
def dynamic_text(text=None):
    """
    Display dynamic text input, and replacing undescore for space
    """
    return ("C {}".format(text.replace('_', ' ')))

@app.route('/python/', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_text(text='is_cool'):
    """
    Display dynamic text, and replace underscore for space
    """
    return ("Python {}".format(text.replace('_', ' ')))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
