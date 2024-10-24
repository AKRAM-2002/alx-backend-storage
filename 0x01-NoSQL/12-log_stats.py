#!/usr/bin/env python3
"""
A script to provide some stats about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient("mongodb://localhost:27017/")
# Use the 'logs' database and 'nginx' collection
db = client['logs']
collection = db['nginx']

# Count total logs in the collection
total_logs = collection.count_documents({})

# Define the methods we're interested in
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

# Print total logs
print(f"{total_logs} logs")

# Print the methods statistics
print("Methods:")
for method in methods:
        method_count = collection.count_documents({'method': method})
        print(f"\tmethod {method}: {method_count}")

# Count the number of status checks (GET requests with path /status)
status_check_count = collection.count_documents({'method': 'GET', 'path': '/status'})
print(f"{status_check_count} status check")

