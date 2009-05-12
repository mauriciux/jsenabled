# -*- coding: utf-8 -*-
"""
Pocket library of Alfred, specilized for JSenabled
"""

# -- MODULES IMPORT --

# system modules
import os
import re

# GAE modules
from google.appengine.ext.webapp import template

# Custom library modules 
import config, service
import validator_config

# -- CUSTOM FUNC DEFINITION --

# template render with django system
def render_template(template_path_from_root, **template_argv):
    """Return rendered template with Django template system provided by GAE."""
    _rendered = template.render(template_path_from_root, template_argv)
    return _rendered

# Validator Class
class Validator(object):
    """Validator class.
    Partialy compatible with Stauren's JS Validator class CONFIG
    """
    # Predefined regExp
    _reg_exp = {
        'email' : r'^([a-zA-Z0-9_\.\-\+])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$',
        'cnPhone' : r'^(\d{3,4}-)\d{7,8}(-\d{1,6})?$',
        'cnMobile' : r'^1[3,5]\d{9}$',
        'yid' : r'^[a-z][a-z_0-9]{3,}(@yahoo\.cn)?$',
        'date' : r'^\d{4}\-[01]?\d\-[0-3]?\d$|^[01]\d\/[0-3]\d\/\d{4}$|^\d{4}Äê[01]?\dÔÂ[0-3]?\d[ÈÕºÅ]$',
        'integer' : r'^[1-9][0-9]*$',
        'number' : r'^[+-]?[1-9][0-9]*(\.[0-9]+)?([eE][+-][1-9][0-9]*)?$|^[+-]?0?\.[0-9]+([eE][+-][1-9][0-9]*)?$',
        'alpha' : r'^[a-zA-Z]+$',
        'alphaNum' : r'^[a-zA-Z0-9_]+$',
        'urls' : r'^(http|https):\/\/(\w+:{0,1}\w*@)?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?$',
        'chinese' : r'^[\u2E80-\uFE4F]+$',
        'postal' : r'^[0-9]{6}$'
    }
    def __init__(self, module_name):
        self.module = validator_config.__dict__[module_name]
    def validate(self, **attr_dict):
        for _key in self.module:
            _flag=True
            if not attr_dict.has_key(_key):
                return False
            else:
                _value_list = attr_dict[_key]
            _rule=self.module[_key]
            if not _rule.get('multi', False):
                _value_list = [_value_list]
            for _value in _value_list:
                #minValue, maxValue, minLength, maxLength
                _flag=(_flag and self.in_period(_value, _rule.get('minValue'), _rule.get('maxValue')))
                _flag=(_flag and self.in_period(_value, _rule.get('minLength'), _rule.get('maxLength'), func=len))
                #mask, useDefined
                if _rule.has_key('mask'):
                    _flag=(_flag and self.search_pattern(_value, _rule['mask']))
                if _rule.has_key('useDefined'):
                    _flag=(_flag and self.search_pattern(_value, self._reg_exp[_rule['useDefined']]))
                #available
                if _rule.has_key('exist'):
                    _flag=(_flag and (self.is_exist(service.__dict__[_rule['exist']['module_name']], **{_rule['exist']['attribute']: _value})==_rule['exist']['accept']))
                if not _flag:
                    return False
        return True
    def search_pattern(self, value, pattern):
        """Search pattern in value, return re.match object or None"""
        _pattern = re.compile(pattern)
        _match = _pattern.search(value)
        return _match
    def in_period(self, value, lower_bound, upper_bound, func=lambda _x: _x):
        """Return True if func(value) in period [lower_bound, upper_bound]"""
        if ((lower_bound==None) and (upper_bound==None)):
            return True
        if (lower_bound==None):
            return func(value) <= upper_bound
        if (upper_bound==None):
            return func(value) >= lower_bound
        return ((func(value) >= lower_bound) and (func(value) <= upper_bound))
    def is_exist(self, class_reference, **key_value):
        """Return True if value exists in class_reference.key
        WARNING: THIS METHOD NEED service.py MODULE
        """
        return True if service.select_from(class_reference, **key_value).get() else False
