#!/usr/bin/env python
# coding: utf-8

# ## MongoDB Database CRUD Operations from Jupyter Notebook with Python:

# #### Interacting with MongoDB using Python via Jupyter Notebook - alternative to IDE or Text Editor.
# 
# **Description**: Here I have written the statements to perform CRUD actions on **customer_details** collection in **mongodb_workshop** database from localhost server of MongoDB.
# 
# #### MongoDB CRUD methods with Python
# 
# **Create/Insert**:
# > - insert_one()
# > - insert_many()
# 
# **Read/Fetch**:
# > - To find all documents - find()
# > - To find one specific document - find({})
# 
# **Update**:
# > - update_one()
# > - update_many()
# 
# **Delete**:
# > - delete_one()
# > - delete_many()

# pip install pymongo

import pymongo

# To connect to MongoDB server:
client = pymongo.MongoClient('localhost', 27017)

# Create Database:
db = client.mongodb_workshop

# Create Collection:
collection = db.collection["coach_details"]

# #### Data to store/insert into MongoDB Database:

# One document:
doc_1 = {"_id": 1, "first_name": "Roldoro", "gender": "M", "shift": ["AM", "PM"], "ph_num": 456378903, "trains_for": ["valleyball", "basketball"], "manager": "Jack"}

# Multiple documents:
docs = [
    {"first_name": "Audrey", "gender": "F", "shift": "AM", "ph_num": 234564980, "trains_for": ["tennis", "badminton"], "manager": "Jack"},
    {"first_name": "William", "gender": "M", "shift": "AM", "ph_num": 987654321, "trains_for": ["valleyball", "basketball"], "manager": "Amin"},
    {"first_name": "Deo", "gender": "M", "shift": "PM", "ph_num": 456234908, "trains_for": "badminton", "manager": "Amin"},
    {"first_name": "Sutton", "gender": "M", "shift": "AM", "ph_num": 123456789, "trains_for": "tennis", "manager": "Jack"},
    {"first_name": "Emma", "gender": "F", "shift": "PM", "ph_num": 776655443, "trains_for": "indoor archery", "manager": "Amin"},
    {"first_name": "Hira", "gender": "F", "shift": ["AM", "PM"], "ph_num": 246813579, "trains_for": ["valleyball", "basketball"], "manager": "Jack"},
    {"first_name": "Isha", "gender": "F", "shift": "PM", "ph_num": 135792468, "trains_for": "indoor archery", "manager": "Amin"},
    {"first_name": "Alice", "gender": "M", "shift": "AM", "ph_num": 2244668800, "trains_for": "badminton", "manager": "Jack"},
    {"first_name": "Deepali", "gender": "F", "shift": ["AM", "PM"], "ph_num": 113355779, "trains_for": ["tennis", "badminton"], "manager": "Amin"}
]

# Dummy documents:
test_docs = [
    {"first_name": "test_1", "gender": "F", "shift": "AM", "ph_num": 234564980, "trains_for": ["tennis", "badminton"], "manager": "Jack"},
    {"first_name": "test_2", "gender": "M", "shift": "AM", "ph_num": 987654321, "trains_for": ["valleyball", "basketball"], "manager": "Amin"},
    {"_id":14, "first_name": "test_3", "gender": "M", "shift": "AM", "ph_num": 987654321, "trains_for": ["valleyball", "basketball"], "manager": "Amin"}
]

# Dummy Document:
test_doc = {"_id":14, "first_name": "test", "gender": "M", "shift": "AM", "ph_num": 987654321, "trains_for": ["valleyball", "basketball"], "manager": "Amin"}

# #### To insert documents to the above collection 'coach_details':

# To insert one document:
collection.insert_one(doc_1)

# To insert multiple documents:
collection.insert_many(docs)

# To insert test documents:
collection.insert_many(test_docs)

# #### To fetch/read documents: 

# To fetch specific document by passing ID:
collection.find_one(1)

# To fetch all documents:
results = collection.find()

# OR
# results = collection.find({})

# To display documents:
for res in results:
    print(res)

# To fetch only few documents:
ans = collection.find({}).limit(3)

# To display documents:
for doc in ans:
    print(doc)

# #### To delete documents:

# To delete one document:
collection.delete_one({"_id": 14})

# To delete selected documents:
del_docs = { "first_name": {"$regex": "^t"} }

collection.delete_many(del_docs)

# To delete all documents - not recommended!
# collection.delete_many({})

# #### To update documents:

# Storing values in variables to be updated/edited:
doc_update = {"first_name": "Deo"}
val_update = {"$set": {"first_name": "Deora"}}

# To update one document:
collection.update_one(doc_update, val_update)

# Storing values in variables to be updated/edited:
docs_update = {"first_name": {"$regex": "^A"}}
vals_update = {"$set": {"coach": "Wilson"}}

# To update multi documents:
collection.update_many(docs_update, vals_update)

# #### To drop/delete a collection - unless it's not required for production or testing!
# 
# > - For Collection to get created by the MongoDB server, atleast one document needs to be inserted.
test_collection = db.collection["test_collection"]

# NameError: name 'ISODate' is not defined
test_collection.insert_one({"name": "Sample Document"})

test_collection.drop()
