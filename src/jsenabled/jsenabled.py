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
from lib import config, service, pocket

# -- CUSTOM CLASS DEFINITION --
class GeneralPage(webapp.RequestHandler):
    pass

# -- PAGE HANDLERS --
class AdminPage(GeneralPage):
    def get(self):
        self.response.out.write(pocket.render_template(config.TEMPLATE_PATH+'admin.html'))
    def post(self):
        if self.request.get('actiontype') == '1':
            _data_dict={
                'name': self.request.get('name'),
                'description': self.request.get('description'),
                'owner': [self.request.get('owner')],
                'type': int(self.request.get('type')),
                }
            if pocket.Validator('validator_Tag').validate(**_data_dict):
                service.add_to(service.Tag, **_data_dict)
                self.response.out.write('Addition successfully')
            else:
                self.response.out.write('Validate failed!')
        elif self.request.get('actiontype') == '2':
            service.delete_from(service.Tag, name=self.request.get('name'))
        elif self.request.get('actiontype') == '3':
            service.modify_on(service.Tag, {'name': self.request.get('fromname')}, {'name': self.request.get('toname')})

class MainPage(GeneralPage):
    def get(self):
        _tags = service.select_from(service.Tag, all=True)
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
