from flask_pymongo import PyMongo
import os
from pymongo import MongoClient
from app.main.config import DevelopmentConfig
# connect local db


MONGO_DBNAME = DevelopmentConfig.MONGO_DBNAME
MONGO_URI = DevelopmentConfig.MONGO_URI
MONGO_LOG = DevelopmentConfig.MONGO_LOG
MONGO_USERNAME = DevelopmentConfig.MONGO_USERNAME
MONGO_PASSWORD = DevelopmentConfig.MONGO_PASSWORD
mongo = MongoClient(MONGO_URI)


def setup_mongo_connection(app):
    global mongo

    MONGO_URL = os.environ.get('MONGO_URL')
    if not MONGO_URL:
        MONGO_URL = MONGO_URI

    app.config['MONGO_DBNAME'] = MONGO_DBNAME
    app.config['MONGO_URI'] = MONGO_URL
    app.config['MONGO_USERNAME'] = MONGO_USERNAME
    app.config['MONGO_PASSWORD'] = MONGO_PASSWORD
    mongo = PyMongo(app)
