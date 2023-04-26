#!/usr/bin/env python3
"""
A Flask application with i18n support
"""


from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__, instance_relative_config=True)
babel = Babel(app)


class Config:
    """
    Configuration class for Babel extension
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """
    Returns the user's preferred local language based on the query string of the
    HTTP request or the user's browser preferences.
    """
    if request.args.get('locale'):
        lang = request.args.get('locale')
        if lang in app.config['LANGUAGES']:
            return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def home() -> str:
    """
    Render the index template
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(debug=True)
