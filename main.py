#!/usr/bin/env python37

import os
import sys

from flask import Flask, render_template
import jinja2
import config
import ee

app = Flask(__name__)

JINJA_ENVIRONMENT = jinja2.Environment(
                                       loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates'),
                                       extensions=['jinja2.ext.autoescape'],
                                       autoescape=True)

@app.route('/')
def MainPage():
    ee.Initialize(config.EE_CREDENTIALS)
    template_values = {}

    return render_template('index.html')

