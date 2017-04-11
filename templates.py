
import os

import webapp2

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

class MainPage(Handler):
    def get(self):
        self.write("Hello, Udacity!")

app = webapp2.WSGIApplication([('/', MainPage),
                                ],
                                debug=True)























# def escape_html(s):
#     chars = {'>': '&gt;', '<':'&lt;', '"':'&quot;', '&':'&amp;'}
#     for i, j in chars.iteritems():
#         s = s.replace(i, j)
#     return s


# import cgi
# def escape_html(s):
#     return cgi.escape(s, quote = True)

# print escape_html('"hello, & = &amp;"')