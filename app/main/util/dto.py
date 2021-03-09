from flask_restplus import Namespace, fields


class welcomeDto:
    api = Namespace('user', description='user related operations')
    welcome = api.model('user', {
        'email': fields.String(required=False, description='user email address'),
        'password': fields.String(required=False, description='user password'),
    })
