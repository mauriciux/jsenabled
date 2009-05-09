"""
Pocket library of Alfred, specilized for JSenabled
"""

# -- MODULES IMPORT --

# system modules
import os
import re

# GAE modules
from google.appengine.ext.webapp import template


# -- CUSTOM FUNC DEFINITION --

# template render with django system
def render_template(template_path_from_root, **template_argv):
    """Return rendered template with Django template system provided by GAE."""
    _rendered = template.render(template_path_from_root, template_argv)
    return _rendered

# Basic validation funcs (pocket part)
def search_pattern(value, pattern):
    """Search pattern in value, return re.match object or None"""
    _pattern = re.compile(pattern)
    _match = _pattern.search(value)
    return _match

def in_period(value, lower_bound, upper_bound, func=lambda _x: _x):
    """Return True if func(value) in period [lower_bound, upper_bound)"""
    return ((func(value) >= lower_bound) and (func(value) < upper_bound))

def can_be_int(value):
    """Return True if value can be converted to int.
    Example: can_be_int(10) # True
             can_be_int(-1) # True
             can_be_int(0.5) # True
             can_be_int('10') # True
             can_be_int('-1') # True
             can_be_int('0.5') # False !
    """
    try:
        int(value)
    except:
        return False
    return True

