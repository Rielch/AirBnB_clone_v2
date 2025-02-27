#!/usr/bin/python3
"""Starts a Flask application and display Hello HBNB!"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello_HBNB():
    """Displays Hello HBNB!"""
    return("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """Displays HBNB"""
    return("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """Displays C followed by the value of text"""
    return("C {}".format(text.replace('_', ' ')))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text="is cool"):
    """Display Python followed by the value of text"""
    return("Python {}".format(text.replace('_', ' ')))


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """Display n is a number if n is an integer"""
    return("{} is a number".format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Displays a HTML template if n is an integer"""
    return(render_template('5-number.html', numb=n))


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """Displays a HTML template deppending if n is even or odd"""
    if n % 2 == 0:
        return (render_template('6-number_odd_or_even.html',
                                numb="{} is even".format(n)))
    else:
        return (render_template('6-number_odd_or_even.html',
                                numb="{} is odd".format(n)))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
