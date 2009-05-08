# Google App Engine
# Project name: JSenabled 
# Owner: Stauren, Woodsprite (Alred)
# Description: A site about JS
#              [more detail]

# -- MODULES IMPORT --

# Python system modules

# Modules provided by GAE
import wsgiref.handlers
from google.appengine.ext import webapp

# Custom library modules 
from lib import config, service, pocket, datadef

# -- CUSTOM CLASS DEFINITION --
class GeneralPage(webapp.RequestHandler):
    pass

# -- PAGE HANDLERS --
class AdminPage(GeneralPage):
    def get(self):
        self.response.out.write(pocket.render_template(config.TEMPLATE_PATH+'admin.html'))
    def post(self):
        if self.request.get('actiontype') == '1':
            service.add_to(datadef.Tag, name=self.request.get('name'), description=self.request.get('description'), owner=[self.request.get('owner')], type=int(self.request.get('type')))
        elif self.request.get('actiontype') == '2':
            service.delete_from(datadef.Tag, name=self.request.get('name'))
        elif self.request.get('actiontype') == '3':
            service.modify_on(datadef.Tag, {'name': self.request.get('fromname')}, {'name': self.request.get('toname')})

class MainPage(GeneralPage):
    def get(self):
        _tags = service.select_from(datadef.Tag, all=True)
        for _tag in _tags:
            self.response.out.write(_tag.to_xml())
    def post(self):
        pass

# -- MAIN FUNC --
def main():
    """main function"""
    wsgiref.handlers.CGIHandler().run(application)

application = webapp.WSGIApplication([('/', MainPage),
                                      ('/admin/', AdminPage)],
                                     debug=True)

if __name__ == '__main__':
    main()
