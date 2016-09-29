from flask import session, redirect, url_for, render_template, request
from . import main

@main.route('/', methods=['GET', 'POST'])
def index():
    """"Controller Main."""
    session['name'] = 'car'
    session['room'] = 'raspberry'
    return render_template('controller.html')
