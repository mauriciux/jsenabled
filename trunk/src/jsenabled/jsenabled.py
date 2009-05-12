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
from lib import interface

# -- CUSTOM CLASS DEFINITION --
class GeneralPage(webapp.RequestHandler):
    pass

# -- PAGE HANDLERS --
class AdminPage(GeneralPage):
    def get(self):
        self.response.out.write(interface.pocket.render_template(interface.config.TEMPLATE_PATH+'admin.html'))
    def post(self):
        if self.request.get('actiontype') == 'addtag':
            _data_dict={
                'name': self.request.get('name'),
                'description': self.request.get('description'),
                'owner': [self.request.get('owner')],
                'type': int(self.request.get('type')),
                }
            if interface.add_tag(**_data_dict):
                self.response.out.write('Addition successfully')
            else:
                self.response.out.write('Validate failed!')
        elif self.request.get('actiontype') == 'deltag':
            if interface.delete_tag(tag_name=self.request.get('name')):
                self.response.out.write('Deletion successfully')
            else:
                self.response.out.write('Deletion failed!') 
        elif self.request.get('actiontype') == 'adduser':
            _data_dict={
                'user_id': self.request.get('user_id'),
                'type': int(self.request.get('type')),
                'password': self.request.get('password'),
                'article_count': int(self.request.get('article_count')),
                'email': self.request.get('email'),
                }
            if interface.add_user(**_data_dict):
                self.response.out.write('Addition successfully')
            else:
                self.response.out.write('Validate failed!')
        elif self.request.get('actiontype') == 'deluser':
            if interface.delete_user(user_id=self.request.get('user_id')):
                self.response.out.write('Deletion successfully')
            else:
                self.response.out.write('Deletion failed!') 

class MainPage(GeneralPage):
    def get(self):
        _tags = interface.select_tag(all=True)
        for _tag in _tags:
            self.response.out.write('<p>Tag->name: %s; description: %s; type= %s; owner= %s</p>' % (_tag.name, _tag.description, _tag.type, ','.join(_tag.owner)))
        _users = interface.select_user(all=True)
        for _user in _users:
            self.response.out.write('<p>User->user_id: %s; article_count: %s; type= %s; email= %s</p>' % (_user.user_id, _user.article_count, _user.type, _user.email))
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
