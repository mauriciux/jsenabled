"""
Datastore model definition module for JSenabled
"""

# -- MODULES IMPORT --

# GAE database module
from google.appengine.ext import db

# -- DB MODEL CLASS DEFINITION --
class User(db.Model):
    """User information."""
    user_id = db.StringProperty(multiline=False)
    password = db.StringProperty(multiline=False)
    type = db.IntegerProperty()
    email = db.StringProperty(multiline=False)
    article_count = db.IntegerProperty()

class Tag(db.Model):
    """Tag information."""
    name = db.StringProperty(multiline=False)
    description = db.StringProperty()
    type = db.IntegerProperty()
    owner = db.StringProperty(multiline=False)

class BaseArticle(db.Model):
    """Basic article properties, should not be instantiate."""
    id_num = db.IntegerProperty()
    post_author_ip = db.IntegerProperty()
    post_author_key = db.StringProperty(multiline=False)
    latest_content_key = db.StringProperty(multiline=False)
    post_date = db.DateTimeProperty(auto_now_add=True)
    type = db.IntegerProperty()

class Variant(db.Model):
    """Modification tracer, should not be instantiate."""
    modify_author_key = db.StringProperty(multiline=False)
    modify_author_ip = db.IntegerProperty()
    modify_date = db.DateTimeProperty(auto_now_add=True)
    traceback_key = db.StringProperty(multiline=False)

class Comment(BaseArticle):
    """Comments of a formal article."""
    ancestor_key = db.StringProperty(multiline=False)

class FormalArticle(BaseArticle, Variant):
    """A variable, titled and tagged article, can have comments, should not be instantiate."""
    title = db.StringProperty(multiline=False)
    tag_list = db.StringListProperty()
    comment_list = db.StringListProperty()

class Archive(FormalArticle):
    """Archive when an article was modified."""
    pass

class LatestArticle(FormalArticle):
    """Latest post."""
    pass

