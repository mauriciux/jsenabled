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

def select_from(class_reference, custom_condition='', **attr_dict):
    """Select records from class_reference.
    Example: select_from(User, name='Ron')
             select_from(User, custom_condition='age<25', name='LeBron')
    Return the class_reference GqlQuery instance.
    """
    if custom_condition == 'all':
        _entries = class_reference.all()
    else:
        #Construct GQL query
        _gql = 'WHERE '+custom_condition
        for _key in attr_dict:
            _gql += ' AND ' + _key + '=' + str(attr_dict[_key])
        _gql = _gql.replace('WHERE  AND', 'WHERE')
        
        #Execute selection
        _entries = class_reference.gql(_gql)

    return _entries
    

def delete_from(class_reference, custom_condition='', **attr_dict):
    """Delete a record from class_reference datastore.
    Example: delete_from(User, name='Kobe')
             delete_from(User, custom_condition='age>30', name='Miller')
    Comments: use custom_condition when inequity is needed.
    Return deleted record amount if succeeded, otherwise return 0.
    """
    #Select GqlQuery
    _entries = select_from(class_reference, custom_condition=custom_condition, **attr_dict)    

    #Execute deletion
    return _entries
