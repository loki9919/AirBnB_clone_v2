#!/usr/bin/python3
""" script that starts a Flask web application:
     web application must be listening on 0.0.0.0, port 5000
     Routes:
        /: display "Hello HBNB!"
        /hbnb: display "HBNB"
        /c/<text>: display “C ” followed by the value of the text variable
                    (replace underscore _ symbols with a space )
        /python/<text>: display “Python ”, followed by the value of the text
                    variable (replace underscore _ symbols with a space )
                The default value of text is “is cool”
     must use the option strict_slashes=False in my route definition
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
        return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
