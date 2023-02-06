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


if __name__== '__main__':
    app.run(host='0.0.0.0', port=5000)
