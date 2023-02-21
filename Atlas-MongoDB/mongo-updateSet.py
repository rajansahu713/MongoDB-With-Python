from pymongo import MongoClient
import pprint
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI=os.getenv('ATLAS_MONGODB_URL')

client = MongoClient(MONGO_URI)

db = client.bank

account_collection = db.details

select_accounts ={"account_type":"saving"}

set_field ={"$set":{"minimum_balance":100}}

result = account_collection.update_many(select_accounts, set_field)

print("Documents matched: ",str(result.matched_count))
print("Documents updated", str(result.modified_count))

pprint.pprint(account_collection.find_one(select_accounts))

client.close()