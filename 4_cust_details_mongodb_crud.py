#!/usr/bin/env python
# coding: utf-8

# ## MongoDB Database Operations from Jupyter Notebook with Python:

# #### Interacting with MongoDB using Python via Jupyter Notebook instead of IDE or Text Editor
# #### MongoDB CRUD commands
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
# from pymongo import MongoClient


client = pymongo.MongoClient('localhost', 27017)
db = client.mongodb_workshop
collection = db.collection["customer_details"]

# #### To insert one document:

cust_1 = {"_id": 1, "first_name": "John", "gender": "M", "mem_type": "gold", "coach": "Roldoro", "batch": "AM", "num_of_sessions_week": 3, "sport_registered": "valleyball", "price_month": 27}

collection.insert_one(cust_1)


# #### To insert more than one document:
cust_docs = [
    {"_id": 2, "first_name": "Abbas", "gender": "F", "mem_type": "gold", "coach": "Roldoro", "batch": "AM", "num_of_sessions_week": 3, "sport_registered": "valleyball", "price_month": 27},
    {"_id": 3, "first_name": "Kate", "gender": "F", "mem_type": "gold", "coach": "Roldoro", "batch": "PM", "num_of_sessions_week": 3, "sport_registered": "basketball", "price_month": 27},
    {"_id": 4, "first_name": "Adnan", "gender": "F", "mem_type": "silver", "coach": "Roldoro", "batch": "PM", "num_of_sessions_week": 2, "sport_registered": "basketball", "price_month": 24},
    {"_id": 5, "first_name": "Kim", "gender": "M", "mem_type": "silver", "coach": "William", "batch": "PM", "num_of_sessions_week": 2, "sport_registered": "badminton", "price_month": 24},
    {"_id": 6, "first_name": "Akhil", "gender": "F", "mem_type": "platinum", "coach": "William", "batch": "PM", "num_of_sessions_week": 4, "sport_registered": "badminton", "price_month": 30},
    {"_id": 7, "first_name": "Madison", "gender": "M", "mem_type": "silver", "coach": "William", "batch": "AM", "num_of_sessions_week": 2, "sport_registered": "tt", "price_month": 24}
]


collection.insert_many(cust_docs)

# #### To fetch all documents from the collection:
collection.find()


results = collection.find()
# OR
# results = collection.find({})

for doc in results:
    print(doc)


# #### To fetch only specific number of documents:
ans = collection.find({}).limit(3)

for doc in ans:
    print(doc)


# #### To fetch the specific document by passing in index/id:
collection.find_one(2)


# #### Insert a record without explicit '_id' property:
# doc_delete = {"first_name": "check", "gender": "M", "mem_type": "gold", "coach": "Roldoro", "batch": "AM", "num_of_sessions_week": 3, "sport_registered": "valleyball", "price_month": 27}

res = collection.insert_one({"first_name": "check", "gender": "M", "mem_type": "gold", "coach": "Roldoro", "batch": "AM", "num_of_sessions_week": 3, "sport_registered": "valleyball", "price_month": 27})

# To get the id of the above inserted document:
res.inserted_id


# #### To delete one document - i.e., above document:
collection.delete_one({"_id": "ObjectId('604f9fd2779a06bb517fcbf3')"})

# To insert document with specific id:
doc_delete = collection.insert_one({"_id": 8, "first_name": "Todelete", "gender": "M", "mem_type": "gold", "coach": "Roldoro", "batch": "AM", "num_of_sessions_week": 3, "sport_registered": "valleyball", "price_month": 27}) 
collection.delete_one({"_id": 8})


# #### To delete more than one document:
del_docs = { "first_name": {"$regex": "^c"} }
collection.delete_many(del_docs)


# #### To delete all the documents:
# collection.delete_many({})


# #### To update one document:
doc_update = {"first_name": "John"}
val_update = {"$set": {"first_name": "Johnson"}}

collection.update_one(doc_update, val_update)


# #### To update more than one document:
docs_update = {"first_name": {"$regex": "^A"}}
vals_update = {"$set": {"coach": "Deo"}}

collection.update_many(docs_update, vals_update)


# #### To drop a collection:
# collection.drop()
