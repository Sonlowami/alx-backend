#!/usr/bin/env python3
"""Create a simple flask appication"""
from flask import Flask, render_template, request
from flask_babel import Babel
from typing import List

app: Flask = Flask(__name__)
babel: Babel = Babel(app)


class Config:
    """Create babel configurations"""

    LANGUAGES: List = ['en', 'fr']
    BABEL_DEFAULT_LOCALE: str = 'en'
    BABEL_DEFAULT_TIMEZONE: str = 'UTC'


app.config.from_object(Config)


@app.route('/')
def index():
    """Return index.html"""
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """Return the language selection to use"""
    locale: str = request.args.get('locale')
    if locale in ['fr', 'en']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run()
