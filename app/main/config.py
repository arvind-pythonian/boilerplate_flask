import os
import configparser
import json

# uncomment the line below for mongodb database url from environment variable
# mongodb_local_base = os.environ['DATABASE_URL']

basedir = os.path.abspath(os.path.dirname(__file__))


# staging configuration path
# _config_dir = os.path.abspath('')
# local configuration path
# _config_dir = os.path.abspath('')
# _parser = configparser.RawConfigParser()
# _parser.read(_config_dir)


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'Please_update_this_key_to_protect_token')
    DEBUG = False,
    TOKEN_EXPIRES_HOURS = os.getenv('TOKEN_EXPIRES_HOURS', 4)


class DevelopmentConfig(Config):
    # IP_ADDRESS = _parser.get('BASIC', 'ip_address')
    # MONGODB_DATABASE_URI = _parser.get('mongo', 'url')
    # MONGO_DBNAME = _parser.get('mongo', 'MONGO_DBNAME')
    # MONGO_URI = MONGODB_DATABASE_URI
    # MONGO_LOG = _parser.get('mongo', 'MONGO_LOG')
    # MONGO_USERNAME = _parser.get('mongo', 'MONGO_USERNAME')
    # MONGO_PASSWORD = _parser.get('mongo', 'MONGO_PASSWORD')
    IP_ADDRESS = ""
    MONGODB_DATABASE_URI = "mongodb://localhost:27017/local"
    MONGO_DBNAME = "local"
    MONGO_URI = "mongodb://localhost:27017/local"
    MONGO_LOG = "mongodb://localhost:27017/log"
    MONGO_USERNAME = ""
    MONGO_PASSWORD = ""
    BASE_PATH = "/api/"


config_by_name = dict(
    dev=DevelopmentConfig
)
token_expires_hours = Config.TOKEN_EXPIRES_HOURS
key = Config.SECRET_KEY
