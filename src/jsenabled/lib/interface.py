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

def delete_tag(tag_name):
    return service.delete_from(service.Tag, name=tag_name)

def select_tag(tag_key=None, tag_name=None, all=False):
    if all:
        return service.select_from(service.Tag, all=True)
    if key:
        return service.Tag.get_by_key_name(tag_key)
    if tag_name:
        return service.select_from(service.Tag, name=tag_name)
    return None

def modify_tag(from_dict, to_dict):
    return service.modify_on(service.Tag, from_dict, to_dict)

def add_user(**attr_dict):
    _validator = pocket.Validator('vUser')
    if _validator.validate(**attr_dict):
        service.add_to(service.User, **attr_dict)
        return True
    return False
