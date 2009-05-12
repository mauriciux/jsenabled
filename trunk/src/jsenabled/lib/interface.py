# -*- coding: utf-8 -*-
"""
Interaction with customers
"""

# -- MODULES IMPORT --

# Custom library modules 
import config, service, pocket

# -- CUSTOM FUNC DEFINITION --

# Datastore manipulation

# Tag
def add_tag(**attr_dict):
    _validator = pocket.Validator('vTag')
    if _validator.validate(**attr_dict):
        service.add_to(service.Tag, **attr_dict)
        return True
    return False

def delete_tag(tag_key=None, tag_name=None):
    if tag_key:
        return service.Tag.get_by_key_name(tag_key).delete()
    if tag_name:
        return service.delete_from(service.Tag, name=tag_name)

def select_tag(tag_key=None, tag_name=None, all=False):
    if all:
        return service.select_from(service.Tag, all=True)
    if tag_key:
        return service.Tag.get_by_key_name(tag_key)
    if tag_name:
        return service.select_from(service.Tag, name=tag_name)
    return None

#def modify_tag(from_dict, to_dict):
#    _validator = pocket.Validator('vTag')
#    if _validator.validate(
#      _entries = service.select_from(service.Tag, from_dict)
#    return service.modify_on(service.Tag, from_dict, to_dict)

# User
def add_user(**attr_dict):
    _validator = pocket.Validator('vUser')
    if _validator.validate(**attr_dict):
        service.add_to(service.User, **attr_dict)
        return True
    return False

def delete_user(user_key=None, user_id=None):
    if user_key:
        return service.User.get_by_key_name(user_key).delete()
    if user_id:
        return service.delete_from(service.User, user_id=user_id)

def select_user(user_key=None, user_id=None, all=False):
    if all:
        return service.select_from(service.User, all=True)
    if user_key:
        return service.User.get_by_key_name(user_key)
    if user_id:
        return service.select_from(service.User, user_id=user_id)
    return None

#def modify_user(from_dict, to_dict):
#    if service.select_from(service.User, **to_dict):
#        return 0 
#    return service.modify_on(service.User, from_dict, to_dict)

# Comment
def add_comment(ancestor_key, **attr_dict):
    _validator = pocket.Validator('vBaseArticle')
    if _validator.validate(**attr_dict):
        _validator = pocket.Validator('vComment')
        if _validator.validate(ancestor_key=ancestor_key, **attr_dict):
            _self_key = service.add_to(service.Comment, ancestor_key=ancestor_key, **attr_dict)
            if _self_key:
                _entry = select_basearticle(basearticle_key=_self_key)
                _entry.comment_list.append(_self_key)
                _entry.put()
                return True
    return False

# BaseArticle
def select_basearticle(basearticle_key=None, basearticle_id_num=None):
    if basearticle_key:
        return service.BaseArticle.get_by_key_name(basearticle_key)
    if basearticle_id_num:
        return service.select_from(service.BaseArticle, id_num=basearticle_id_num)
    return None

