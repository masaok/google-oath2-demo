
import webapp2
import os
import jinja2
import json
import datetime
import time
from google.appengine.api import users
from google.appengine.ext import ndb

# from data import Course, Teacher, User, Post, Enrollment

# from content_manager import populate_feed, logout_url, login_url

from pprint import pprint, pformat

jinja_env = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
  extensions=['jinja2.ext.autoescape'],
  autoescape=True)

# the handler section
class MainPage(webapp2.RequestHandler):
  def get(self): #for a get request
    # self.response.headers['Content-Type'] = 'text/plain'
    # self.response.write('Hello, World!') #the response

    template= jinja_env.get_template("/templates/home.html")
    # self.response.write(template.render(get_auth()))
    self.response.write(template.render())

# the app configuration section
app = webapp2.WSGIApplication([
  ('/', MainPage),
], debug=True)
