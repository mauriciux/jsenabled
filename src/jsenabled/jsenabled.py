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

# -- API HANDLERS --
# User
class AddUser(GeneralPage):
    def get(self):
        pass
    def post(self):
        _data = interface.service.make_entity_dict(interface.service.User, {}, self.request)
        self.response.out.write(interface.pocket.toggle(interface.add_user(**_data), interface.config.SUCCEEDED, interface.config.FAILED))

class DelUser(GeneralPage):
    def get(self):
        pass
    def post(self):
        _data = {'user_id': self.request.get('user_id')}
        self.response.out.write(interface.pocket.toggle(interface.delete_user(**_data), interface.config.SUCCEEDED, interface.config.FAILED))

class ModifyUser(GeneralPage):
    def get(self):
        pass
    def post(self):
        _data = interface.pocket.make_transection(interface.service.User.properties(), self.request) 
        self.response.out.write(interface.pocket.toggle(interface.modify_user(from_user_id=self.request.get('from_user_id'), **_data), interface.config.SUCCEEDED, interface.config.FAILED))

# Tag 
class AddTag(GeneralPage):
    def get(self):
        pass
    def post(self):
        _data = interface.service.make_entity_dict(interface.service.Tag, {}, self.request)
        _flag = True
        _owners = []
        for _owner in _data['owner'].split(','):
            _key = interface.service.get_key(interface.service.User, user_id = _owner)
            if _key:
                _owners.append(_key)
            else:
                _flag = False
        if _flag:
            _data['owner'] = _owners
            self.response.out.write(interface.pocket.toggle(interface.add_tag(**_data), interface.config.SUCCEEDED, interface.config.FAILED))
        else:
            self.response.out.write(interface.config.FAILED)

class DelTag(GeneralPage):
    def get(self):
        pass
    def post(self):
        _data = {'name': self.request.get('name')}
        self.response.out.write(interface.pocket.toggle(interface.delete_tag(**_data), interface.config.SUCCEEDED, interface.config.FAILED))

class ModifyTag(GeneralPage):
    def get(self):
        pass
    def post(self):
        _data = interface.pocket.make_transection({'name': None,'description': None}, self.request)
        self.response.out.write(interface.pocket.toggle(interface.modify_tag(from_name=self.request.get('from_name'), **_data), interface.config.SUCCEEDED, interface.config.FAILED))

# -- PAGE HANDLERS --
class AdminPage(GeneralPage):
    def get(self):
        self.response.out.write(interface.pocket.render_template(interface.config.TEMPLATE_PATH+'admin.html'))
    def post(self):
        if self.request.get('actiontype') == 'addlatestarticle':
            _data_dict={
                'id_num': self.request.get('id_num'),
                'post_author_ip': '127.0.0.1',
                'post_author_key': self.request.get('author'),
                'latest_content_key': self.request.get('content'),
                'post_date': self.request.get('date'),
                'type': 1,
                'modify_date': '12-01-1999',
                'modify_author_key': self.request.get('author'),
                'modify_author_ip': '127.0.0.1',
                'traceback_key': self.request.get('content'),
                'title': self.request.get('title'),
                'comment_list': [],
                'tag_list': []
                }
            if interface.add_latestarticle(**_data_dict):
                self.response.out.write('Add successfully')
            else:
                self.response.out.write('Validate failed!')


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
                                      ('/admin/', AdminPage),
                                      ('/adduser/', AddUser),
                                      ('/deluser/', DelUser),
                                      ('/modifyuser/', ModifyUser),
                                      ('/addtag/', AddTag),
                                      ('/deltag/', DelTag),
                                      ('/modifytag/', ModifyTag)],
                                     debug=True)

if __name__ == '__main__':
    main()
