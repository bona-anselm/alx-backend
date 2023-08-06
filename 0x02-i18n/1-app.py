#!/usr/bin/env python3
""" Creates basic flask app """
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config():
    """ COnfig files """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFUALT_LOCALE = "en"
    BABEL_DEFUALT_TIMEZONE = "UTC"


app.config.from_object(Config)
app.url_map.strict_slashes = False


@app.route('/')
def index() -> str:
    """ Home route """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()
