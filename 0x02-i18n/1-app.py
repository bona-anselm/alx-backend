#!/usr/bin/env python3
""" Creates basic flask app """
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ COnfig files """
    LANGUAGES = ["en", "fr"]
    DEFUALT_LOCALE = "en"
    DEFUALT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def index():
    """ Home route """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()
