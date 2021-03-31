import pymongo

# To connect to MongoDB server:
client = pymongo.MongoClient('localhost', 27017)

# Create Database:
db = client.mongodb_workshop

# To create collection:
test_collection = db.collection["test_collection"]

# For Collection to get created by the MongoDB server, atleast one document needs to be inserted:
test_collection.insert_one({"name": "Sample Document"})

# To delete collection:
test_collection.drop()