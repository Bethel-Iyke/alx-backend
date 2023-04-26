#!/usr/bin/env python3
"""A flask app application
"""


from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def language_conf() -> str:
    """Configuration class that instantiates babe,
    configure avalable language using ["en", "fr"].
    """
    return render_template('1-index.html')


class Config(object):
    """Babel instance to configure available
        and a selector
        Languages ["en", "fr"]
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


if __name__ == ('__main__'):
    app.run()
