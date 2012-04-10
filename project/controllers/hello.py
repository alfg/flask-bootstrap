#!/usr/bin/env python

from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)

# Lazy view from views module
def hello_world():
    return 'Hello World!'
