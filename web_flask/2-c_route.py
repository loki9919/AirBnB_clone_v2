#!/usr/bin/python3
""" script that starts a Flask web application:
     web application must be listening on 0.0.0.0, port 5000
     Routes:
        /: display "Hello HBNB!"
        /hbnb: display "HBNB"
        /c/<text>: display “C ” followed by the value of the text variable
                    (replace underscore _ symbols with a space )
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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
