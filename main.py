import os

import sys

import webapp2
import jinja2
import config
#import pycrypto
import ee



JINJA_ENVIRONMENT = jinja2.Environment(
                                       loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates'),
                                       extensions=['jinja2.ext.autoescape'],
                                       autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        ee.Initialize(config.EE_CREDENTIALS)
        template_values = {}
        #ee.Initialize();
        
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))
        #self.response.headers['Content-Type'] = 'text/plain'
        #self.response.write('Hello, World!')


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
