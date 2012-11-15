#!/usr/bin/env python

from project import urls
from project import config

# app = GUnicorn Hook
app = urls.app
app.config['DEBUG'] = config.DEBUG
