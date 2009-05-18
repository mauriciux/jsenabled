"""
Validator config module
"""

vUser = {
    'user_id': {
        'maxLength': 15,
        'minLength': 6,
        'exist': {
            'accept': False,
            'module_name': 'User',
            'attribute': 'user_id'
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
        'value_type': int,
        'minValue': 0,
        'maxValue': 10
        },
    'article_count': {
        'value_type': int,
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
        },
    'type': {
        'value_type': int,
        'minValue': 0,
        'maxValue': 10
        },
    'owner': {
        'multi': True,
        'key': {
            'module_name': 'User',
            'attribute': 'user_id'
            },
        'exist': {
            'accept': True,
            'module_name': 'User',
            'attribute': 'user_id'
            }
        }
    }

vBaseArticle = {
    'id_num': {
        'value_type': int,
        'minValue': 0
        },
    'post_author_ip': {
        'minValue': 0
        },
    'post_date': {
        'mask': r'^[12]\d{3}\-[01]\d\-[0-3]\d$'
        },
    'type': {
        'value_type': int,
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

