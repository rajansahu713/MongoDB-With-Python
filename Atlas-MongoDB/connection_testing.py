from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

# We are using atlas mongodb
MONGO_URI=os.getenv('ATLAS_MONGODB_URL')

client = MongoClient(MONGO_URI)

# Printing all the existing databases
for db_name in client.list_database_names():
    print(db_name)

