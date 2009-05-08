"""
Pocket library of Alfred, specilized for JSenabled
"""

# -- MODULES IMPORT --

# system modules
import os

# GAE modules
from google.appengine.ext.webapp import template


# -- CUSTOM FUNC DEFINITION --

def render_template(template_path_from_root, **template_argv):
    """Return rendered template with Django template system provided by GAE."""
    _rendered = template.render(template_path_from_root, template_argv)
    return _rendered 
