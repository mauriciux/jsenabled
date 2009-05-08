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
    return True

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
        _del+=1
    return _del
