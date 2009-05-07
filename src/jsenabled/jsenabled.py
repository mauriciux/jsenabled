# Google App Engine
# Project name: JSenabled 
# Owner: Stauren, Woodsprite (Alred)
# Description: A site about JS
#              [more detail]

# -- MODULES IMPORT --

# Python system module

# Request handler modules provided by GAE
import wsgiref.handlers
from google.appengine.ext import webapp

# Database Model module
from lib.datadef import *

# -- PAGE HANDLERS --
class MainPage(webapp.RequestHandler):
    def get(self):
        _test=LatestArticle()
        _test.title = "Let's go!"
        _test.id_num = 1234
        self.response.out.write(_test.to_xml())
    def post(self):
        pass

# -- MAIN FUNC --
def main():
    """main function"""
    wsgiref.handlers.CGIHandler().run(application)

application = webapp.WSGIApplication([('/', MainPage)],
                                     debug=True)

if __name__ == '__main__':
    main()
