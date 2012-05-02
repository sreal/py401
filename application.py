import logging
import base64

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
    def get(self):
        logging.info("....remote_addr: %s" % self.request.remote_addr)
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write('\
Welcome.<br />\
Basic Authenticaion Test Server<br />\
<br />\
<a href="/401">/401</a>\
<br />\
<br />\
--sre')

class BasicAuth(webapp.RequestHandler):
    def get(self):
        logging.info("....remote_addr: %s" % self.request.remote_addr)
        if not 'Authorization' in self.request.headers:
            self.Send401()
        else:
            auth = self.request.headers['Authorization']
            (username, password) = base64.b64decode(auth.split(' ')[1]).split(':')
            logging.info("....usr: %s" % username)
            logging.info("....pwd: %s" % password)
            if username == 'usr' and password == 'pwd':
                self.response.out.write("Authentication Successful")
            else : 
                self.Send401()

    def Send401(self):
        self.response.clear()
        self.response.headers['WWW-Authenticate'] = 'Basic realm="usr:pwd"'
        self.response.set_status(401)
        self.response.out.write("Authorization required")

application = webapp.WSGIApplication(
                                     [('/',    MainPage),
                                      ('/401', BasicAuth)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()