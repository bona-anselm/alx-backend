#!/usr/bin/env python3
""" Creates basic flask app """
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


class Config():
    """ COnfig files """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


babel = Babel(app)
app.config.from_object(Config)
app.url_map.strict_slashes = False


@app.route('/')
def index() -> str:
    """ Home route """
    return render_template("4-index.html")


@babel.localeselector
def get_locale() -> str:
    """
        Selects & determines the best match with our supported languages
    """
    locale = request.args.get("locale")
    if locale and locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(port=8080)
