from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Welcome. This is a Basic Authenticaion Test Server')
class 401Test(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('401')

application = webapp.WSGIApplication(
                                     [('/',    MainPage)],
                                     [('/401', BasicAuth)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()