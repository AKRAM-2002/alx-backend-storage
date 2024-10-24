#!/usr/bin/env python3
"""
function that inserts a new document
in a collection based on kwargs
"""

def insert_school(mongo_collection, **kwargs):
    '''Inserts a new document in a collection.
    '''
    result = mongo_client.insert(kwargs)
    return result.inserted_id
