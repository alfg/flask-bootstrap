#!/usr/bin/env python

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from project import config


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "%s://%s:%s@%s/%s" % (config.DBTYPE, config.DBUSER, config.DBPASS, config.DBHOST, config.DBNAME)
db = SQLAlchemy(app)

# Create models from tables here
class Tablename(db.Model):
    column_one = db.Column(db.Integer, primary_key=True)
    column_two = db.Column(db.String(80))

    def __init__(self, column_one, column_two):
        self.column_one = column_one
        self.column_two = column_two

    def __repr__(self):
        return '<Table %r>' % self.column_one


