#!/usr/bin/env python
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os, sys
import webapp2
import jinja2
import urllib
from google.appengine.ext import ndb
from notes import my_notes

reload(sys)  
sys.setdefaultencoding('utf8')

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True )

output_message=""

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q=" + text_to_check)
    output = connection.read()
    connection.close()
    if "true" in output:
        return True
    else:
        return False

def user_input_verification(guestbook_name, content):
    if (not content):
        return "The Comment field was blank. Please enter your comments!"
    elif check_profanity(guestbook_name + " " + content):
        return "Please use appropriate words!"
    else:
        return False

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
		self.response.write(*a, **kw)
	
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)
	
    def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

class Greeting(ndb.Model):
    """Models an individual Guestbook entry with author, content and date."""
    author = ndb.StringProperty(indexed=False)
    content = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def query_book(cls, ancestor_key):
        return cls.query(ancestor=ancestor_key).order(-cls.date)

class MainHandler(Handler):
    def get(self):
        ancestor_key = ndb.Key("Book", "*notitle*")
        greetings = Greeting.query_book(ancestor_key).fetch(20)
        List_of_greetings = []
        for greeting in greetings: List_of_greetings.append([greeting.author, greeting.content])
        self.render("index8.html", my_notes = my_notes, List_of_greetings = List_of_greetings)

class SubmitForm(Handler):
    def post(self):
        guestbook_name = self.request.get('guestbook_name')
        content = self.request.get('content')
        global output_message
        output_message = user_input_verification(guestbook_name, content)
        if output_message:
            self.redirect('/message')
        else:
            greeting = Greeting(parent=ndb.Key("Book", "*notitle*"),
                                content=content,
                                author=guestbook_name)
            greeting.put()
            self.redirect('/?'
                    + urllib.urlencode({'guestbook_name': guestbook_name})
                      )
    	
class SendMessage(Handler):
    def get(self):
        self.render("message.html", output_message = output_message)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/sign', SubmitForm),
    ('/message', SendMessage)
])
