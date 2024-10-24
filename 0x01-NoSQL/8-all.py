#!/usr/bin/env python3
"""
lists all documents in a collection
"""
from pymongo import MongoClient

def list_all(mongo_collection):
    """
    Lists all documents in a collection
    """
    return [doc for doc in mongo_collection.find()]
