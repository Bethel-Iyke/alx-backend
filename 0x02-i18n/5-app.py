#!/usr/bin/env python3
"""Basic flask app Module
    Get locale from request
    get_locale function with the babel.localeselector
"""


from collections import UserDict
from flask import Flask, g, render_template, request
from flask_babel import Babel

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}
app = Flask(__name__)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def Home() -> str:
    """Home Route renders 5-index.html
        get_locale function with the
        babel.localeselector decorator
    """
    return render_template('5-index.html')


class Config(object):
    """Babel instance to configure available
        and a selector
        Languages ["en", "fr"]
        localeselector decorator:
            nvoked for each request to select a
            language translation to use for that request
    """
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
    LANGUAGES = ["en", "fr"]


def get_local() -> str:
    """babel.localeselector decorator. Uses
        request.accept_languages to
        determine the best match with our supported languages.
    """
    if request.args.get('locale'):
        lang = request.args.get('locale')
        if lang in app.config['LANGUAGES']:
            return lang
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> dict:
    """get_user function to mock a database
        lookup
    """
    userId = request.args.get('login_as', None)
    if userId:
        return users.get(int(userId))
    return None


@app.before_request
def before_request():
    """find a user if any, and set it as a
        global on flask.g.user
    """
    g.user = get_user()


if __name__ == ('__main__'):
    app.run()
