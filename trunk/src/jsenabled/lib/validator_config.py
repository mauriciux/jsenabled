"""
Validator config module
"""

validator_User = {
    'name': {
        'maxLength': 15,
        'minLength': 6,
        'available': 'User' 
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

validator_Tag = {
    'name': {
        'maxLength': 15,
        'minLength': 6,
        'available': 'Tag'
        },
    'description': {
        'maxLength': 250,
        'useDefined': 'email'
        },
    'type': {
        'minValue': 0,
        'maxValue': 10
        }
    }

validator_BaseArticle = {
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

validator_Variant = {
    'modify_date': {
        'mask': r'^[12]\d{3}\-[01]\d\-[0-3]\d$'
        },
    'modify_author_ip': {
        'minValue': 0
        },
    }

validator_Comment = {
    }

validator_FormalArticle = {
    'title': {
        'minLength': 1,
        'maxLength': 100
        }
    }

validator_Archive = {
    }

validator_LatestArticle = {
    }

