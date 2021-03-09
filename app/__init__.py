from flask import Blueprint
from flask_restplus import Api
from app.main import DevelopmentConfig
from .main.controller.welcome_controller import api as welcome_ns

blueprint = Blueprint('api', __name__)
basePath = DevelopmentConfig.BASE_PATH

api = Api(blueprint,
          title='sample',
          version='1.0',
          description='sample'
          )
api.add_namespace(welcome_ns, path='/user')
