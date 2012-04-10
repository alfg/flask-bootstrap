#!/usr/bin/env python

from setuptools import setup

setup(name='project',
      version='0.1',
      description='A New Project',
      author='Peter Gunn',
      author_email='email@example.com',
      packages=['project'],
      install_requires=['Flask', 'flask-sqlalchemy']
)

