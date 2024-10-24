#!/usr/bin/env python3:wq
from pymongo import MongoClient

# Create a MongoClient to the running mongod instance
client = MongoClient("mongodb://localhost:27017/")  # Change the URI as needed

# Connect to a specific database (this will create it if it doesn't exist)
db = client['mydatabase']

# Create or access a collection
collection = db['mycollection']

# Insert a single document
result = collection.insert_one({"name": "Alice", "age": 25})

# Insert multiple documents
result = collection.insert_many([
        {"name": "Bob", "age": 30},
            {"name": "Charlie", "age": 35}
            ])
# Find one document
document = collection.find_one({"name": "Alice"})
print(document)

# Find all documents
all_documents = collection.find()

print("All Documents: ")
for doc in all_documents:
        print(doc)

# Query with filters
filtered_documents = collection.find({"age": {"$gt": 28}})  # age greater than 28
    
print("Above 28 of age: ")    
for doc in filtered_documents:
    print(doc)

client.close()

