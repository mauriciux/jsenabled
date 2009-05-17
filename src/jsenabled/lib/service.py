"""
Service API module for JSenabled datastore manipulation. (ADSM)
"""

# -- MODULES IMPORT --

# datadef module
from datadef import *

# -- Datastore ADSM method --
def add_to(class_reference, **attr_dict):
    """Add a record to class_reference datastore.
    Example: add_to(Tag, name='rockets', description='NBA team in Houston')
    Return True if succeeded.
    """ 
    _entry=class_reference()
    for _key in attr_dict:
        _entry.__dict__['_'+_key] = attr_dict[_key]
    _entry.put()
    return _entry.key()

def select_from(class_reference, all=False, custom_condition='', **attr_dict):
    """Select records from class_reference.
    Example: select_from(User, name='Ron')
             select_from(User, all=True)
             select_from(User, custom_condition='age<25', name='LeBron')
    Return the class_reference GqlQuery instance, (In fact return Query instance if all==True).
    """
    if all:
        _entries = class_reference.all()
    else:
        _gql = 'WHERE ' + ' AND '.join([_key + '=:' + _key for _key in attr_dict])
        if custom_condition != '':
            _gql += ' AND ' + custom_condition
        _entries = class_reference.gql(_gql, **attr_dict)
    return _entries
    

def delete_from(class_reference, custom_condition='', **attr_dict):
    """Delete a record from class_reference datastore.
    Example: delete_from(User, name='Kobe')
             delete_from(User, custom_condition='age>30', name='Miller')
    Comments: use custom_condition when inequity is needed.
    Return deleted record amount if succeeded, otherwise return 0.
    """
    _entries = select_from(class_reference, custom_condition=custom_condition, **attr_dict)    
    _del = 0
    for _entry in _entries:
        _entry.delete()
        _del += 1
    return _del

def modify_on(class_reference, from_dict, to_dict, all=False, custom_condition='', custom_function=False):
    """Modify a record of class_reference
    Example: modify_on(User, {'name': 'Shaq'}, {'name': 'Yao'})
             modify_on(User, {'name': 'Shaq'}, {'name': 'Yao'}, custom_condition='age>35')
             modify_on(User, {}, {'team': 'Rockets'}, all=True)
             modify_on(User, {}, {'age': lambda _age: _age+1}, all=True, custom_function=True)
    Return modified record amount if succeeded, otherwise return 0.
    """
    _entries = select_from(class_reference, all, custom_condition, **from_dict)
    _modify = 0
    if custom_function:
        for _entry in _entries:
            for _key in to_dict:
                _entry.__dict__['_'+_key] = to_dict[_key](_entry.__dict__['_'+_key])
            _entry.put()
            _modify += 1
    else:
        for _entry in _entries:
            for _key in to_dict:
                _entry.__dict__['_'+_key] = to_dict[_key]
            _entry.put()
            _modify += 1
    return _modify
