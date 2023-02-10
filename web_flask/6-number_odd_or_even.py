#!/usr/bin/python3
"""
Starts a Flask Web Application
"""

from flask import Flask, render_template
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


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_text(text='is_cool'):
    """
    Display dynamic text, and replace underscore for space
    """
    return ("Python {}".format(text.replace('_', ' ')))


@app.route('/number/<int:n>', strict_slashes=False)
def dynamic_digits(n=None):
    """
    Display dynamically input number, dont accept none-number
    """
    return ("{} is a number".format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def first_template(n=None):
    """
    Display a HTML page only if input number, n is an integer
    """
    return (render_template('5-number.html', n=n))


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def conditional_template(n=None):
    """
    Display a HTML page only if input number, n is an integer odd or even
    """
    return (render_template('6-number_odd_or_even.html', n=n))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
