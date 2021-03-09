import os
import unittest
from flask_cors import CORS
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app.main.mongo_config import setup_mongo_connection
from app import blueprint
from app.main import create_app  # , db

app = create_app(os.getenv('PROJECT_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()
setup_mongo_connection(app)
CORS(app)

# gunicorn --bind 0.0.0.0:5000 wsgi:app
if __name__ == "__main__":
    env = os.getenv('PROJECT_ENV')
    if env == None:
        os.environ['PROJECT_ENV'] = 'dev'
    app.run()
