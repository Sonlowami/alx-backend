#!/usr/bin/env python3
"""Create a simple flask appication"""
from flask import Flask, render_template


app: Flask = Flask(__name__)


@app.route('/')
def index():
    """Return index.html"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
