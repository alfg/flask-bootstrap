#!/usr/bin/env python

from flask import Flask
from flask import request
from flask import render_template

from project import config
from project.models import *
from project.controllers import hello

app = Flask(__name__)


# All views below
@app.route("/")
def index():

    return render_template('starter-template.html')

@app.route("/fluid")
def fluid():

    return render_template('fluid.html')

@app.route("/hero")
def hero():

    return render_template('hero.html')

@app.route("/layout")
def layout():

    return render_template('layout-template.html')


# Error Pages
@app.errorhandler(500)
def error_page(e):
    return render_template('error_pages/500.html'), 500

@app.errorhandler(404)
def not_found(e):
    return render_template('error_pages/404.html'), 404


# Lazy Views
app.add_url_rule('/hello', view_func=hello.hello_world)



