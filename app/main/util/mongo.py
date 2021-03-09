from pymodm.connection import connect
from app import DevelopmentConfig

DEFAULT_CONNECTION_ALIAS = 'giantcell'


def _get_connection(alias=DEFAULT_CONNECTION_ALIAS):
    """Return a `ConnectionInfo` by connection alias."""
    try:

        # Connect to MongoDB and call the connection "my-app".
        return connect("mongodb://mongo:27017/{}".format(DevelopmentConfig.MONGO_DBNAME), alias="my-app")
    except Exception as e:
        print(e)


"""
from pymongo import MongoClient # import mongo client to connect  
import pprint  
# Creating instance of mongoclient  
client = MongoClient()  
# Creating database  
db = client.giantcell  
user = {"id": "101",  
"username": "peter@example.com",
"password": "Peter",
"email": "peter@example.com",
"deleted": "false"
}  
# Creating document  
users = db.users  
# Inserting data  
users.insert_one(user)  
# Fetching data  
pprint.pprint(users.find_one())  

"""