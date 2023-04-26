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
    return render_template('6-index.html')


class Config(object):
    """Babel instance to configure available
        and a selector
        Languages ["en", "fr"]
        localeselector decorator:
            invoked for each request to select a
            language translation to use for that request
    """
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
    LANGUAGES = ["en", "fr"]

    @staticmethod
    def get_locale():
        if g.get('lang_code', None) is not None:
            return g.lang_code
        user = g.get('user', None)
        if user is not None:
            return user.locale
        accept_languages = request.accept_languages.best_match(
            Config.LANGUAGES)
        return accept_languages


def get_local() -> str:
    """
    Tries to get the language from the following sources in order:
    1. URL parameters (e.g. ?locale=en)
    2. User settings (e.g. g.user['locale'])
    3. Request header (e.g.
    request.accept_languages.best_match(app.config['LANGUAGES']))
    4. Default locale (e.g. app.config['BABEL_DEFAULT_LOCALE'])
    Returns:
        str: The best matching language for the user.
    1. checking for URL parameter
    2. Check user settings
    3. Check request header
    4. Fallback to default locale
    """
    if request.args.get('locale') and request.args.get(
            'locale') in app.config['LANGUAGES']:
        return request.args.get('locale')

    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')

    language = request.accept_languages.best_match(app.config['LANGUAGES'])
    if language and language in app.config['LANGUAGES']:
        return language

    return app.config['BABEL_DEFAULT_LOCALE']


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
