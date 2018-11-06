from flask import request, render_template
from . import main

@main.route('/')
def index():
    return render_template('main/index.html')