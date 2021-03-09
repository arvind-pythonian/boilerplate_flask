from flask import Flask
from flask_bcrypt import Bcrypt
from pymodm import connect

from app.main.config import DevelopmentConfig, config_by_name

flask_bcrypt = Bcrypt()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    config = config_by_name[config_name]

    if config and config.MONGODB_DATABASE_URI:
        app.config["MONGO_URI"] = config.MONGODB_DATABASE_URI
    else:
        app.config["MONGO_URI"] = "mongodb://mongo:27017/{}".format(DevelopmentConfig.MONGO_DBNAME)
    connect(app.config["MONGO_URI"], alias="giantcell")
    flask_bcrypt.init_app(app)
    return app
