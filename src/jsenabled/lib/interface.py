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

def delete_tag(key=None, name=None):
    if key:
        return service.Tag.get_by_key_name(key).delete()
    if name:
        return service.delete_from(service.Tag, name=name)

def select_tag(key=None, name=None, all=False):
    if all:
        return service.select_from(service.Tag, all=True)
    if key:
        return service.Tag.get_by_key_name(key)
    if name:
        _entry = service.select_from(service.Tag, name=name)
        return (_entry.get() if _entry else None)
    return None

def modify_tag(from_key=None, from_name=None, **attr_dict):
    _validator = pocket.Validator('vTag')
    _entry = select_tag(key=from_key, name=from_name)
    if _entry:
        _dict = _entry.__dict__
        _from_dict = _entry.properties()
        for _key in _from_dict:
            _from_dict[_key] = _dict['_'+_key]
        _to_dict = dict(_from_dict)
        _to_dict.update(attr_dict)
        return (service.modify_on(service.Tag, _from_dict, _to_dict) if _validator.validate(**_to_dict) else 0)
    return 0 

# User
def add_user(**attr_dict):
    _validator = pocket.Validator('vUser')
    if _validator.validate(**attr_dict):
        service.add_to(service.User, **attr_dict)
        return True
    return False

def delete_user(key=None, user_id=None):
    if key:
        return service.User.get_by_key_name(key).delete()
    if user_id:
        return service.delete_from(service.User, user_id=user_id)

def select_user(key=None, user_id=None, all=False):
    if all:
        return service.select_from(service.User, all=True)
    if key:
        return service.User.get_by_key_name(key)
    if user_id:
        _entry = service.select_from(service.User, user_id=user_id)
        return (_entry.get() if _entry else None)
    return None

def modify_user(from_key=None, from_user_id=None, **attr_dict):
    _validator = pocket.Validator('vUser')
    _entry = select_user(key=from_key, user_id=from_user_id)
    if _entry:
        _dict = _entry.__dict__
        _from_dict = _entry.properties()
        for _key in _from_dict:
            _from_dict[_key] = _dict['_'+_key]
        _to_dict = dict(_from_dict)
        _to_dict.update(attr_dict)
        return (service.modify_on(service.User, _from_dict, _to_dict) if _validator.validate(**_to_dict) else 0)
    return 0 


# BaseArticle
def select_basearticle(key=None, id_num=None):
    if key:
        return service.BaseArticle.get_by_key_name(key)
    if id_num:
        return service.select_from(service.BaseArticle, id_num=id_num)
    return None

# Comment
def add_comment(ancestor_key, **attr_dict):
    _validator = pocket.Validator('vBaseArticle')
    if _validator.validate(**attr_dict):
        _validator = pocket.Validator('vComment')
        if _validator.validate(ancestor_key=ancestor_key, **attr_dict):
            _self_key = service.add_to(service.Comment, ancestor_key=ancestor_key, **attr_dict)
            if _self_key:
                _entry = select_basearticle(key=_self_key)
                _entry.comment_list.append(_self_key)
                _entry.put()
                return True
    return False

# LatestArticle
def add_latestarticle(**attr_dict):
    _validator1 = pocket.Validator('vBaseArticle')
    _validator2 = pocket.Validator('vFormalArticle')
    _validator3 = pocket.Validator('vLatestArticle')
    if (_validator1.validate(**attr_dict) and _validator2.validate(**attr_dict) and _validator3.validate(**attr_dict)):
        service.add_to(service.LatestArticle, **attr_dict)
        return True
    return False
