"""
Validator config module
"""

vUser = {
    'name': {
        'maxLength': 15,
        'minLength': 6,
        'exist': {
            'accept': False,
            'module_name': 'User',
            'attribute': 'name'
            }
        },
    'password': {
        'maxLength': 15,
        'minLength': 5
        },
    'email': {
        'useDefined': 'email'
        },
    'type': {
        'minValue': 0,
        'maxValue': 10
        },
    'article_count': {
        'minValue': 0,
        }
    }

vTag = {
    'name': {
        'maxLength': 15,
        'minLength': 6,
        'exist': {
            'accept': False,
            'module_name': 'Tag',
            'attribute': 'name'
            }
        },
    'description': {
        'maxLength': 250,
        'useDefined': 'email'
        },
    'type': {
        'minValue': 0,
        'maxValue': 10
        },
    'owner': {
        'exist': {
            'accept': True,
            'module_name': 'User',
            'attribute': 'name'
            }
        }
    }

vBaseArticle = {
    'id_num': {
        'minValue': 0
        },
    'post_author_ip': {
        'minValue': 0
        },
    'post_date': {
        'mask': r'^[12]\d{3}\-[01]\d\-[0-3]\d$'
        },
    'type': {
        'minValue': 0,
        'maxValue': 10
        }
    }

vVariant = {
    'modify_date': {
        'mask': r'^[12]\d{3}\-[01]\d\-[0-3]\d$'
        },
    'modify_author_ip': {
        'minValue': 0
        },
    }

vComment = {
    }

vFormalArticle = {
    'title': {
        'minLength': 1,
        'maxLength': 100
        }
    }

vArchive = {
    }

vLatestArticle = {
    }

