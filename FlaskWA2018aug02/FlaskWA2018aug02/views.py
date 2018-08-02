"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWA2018aug02 import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='IS&P DT&IoT Dept',
        year=datetime.now().year,
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='ntellistok Demo Web Application created with Flask Micro Framework'
    )
