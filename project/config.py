#!/usr/bin/env python

from ConfigParser import SafeConfigParser

config = SafeConfigParser()
config.read('config.ini')

# Read config.ini and store into variables
HOST = config.get('app', 'HOST')
PORT = int(config.get('app', 'PORT'))
DEBUG = config.get('app', 'DEBUG')

DBTYPE = config.get('database', 'DBTYPE')
DBHOST = config.get('database', 'DBHOST')
DBNAME = config.get('database', 'DBNAME')
DBUSER = config.get('database', 'DBUSER')
DBPASS = config.get('database', 'DBPASS')
