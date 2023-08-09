#!/usr/bin/env python3
""" Creates basic flask app """
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config():
    """ COnfig files """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)
app.url_map.strict_slashes = False

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.route('/')
def index() -> str:
    """ Home route """
    return render_template("5-index.html")


@babel.localeselector
def get_locale() -> str:
    """
        Selects & determines the best match with our supported languages
    """
    locale = request.args.get("locale")
    if locale and locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user(user_id):
    """ fetches users from mock db """
    return users.get(user_id)


@app.before_request
def before_request():
    """ before request function """
    user_id = request.args.get('login_as')
    g.user = get_user(int(user_id)) if user_id else None


if __name__ == "__main__":
    app.run(port=8080)
