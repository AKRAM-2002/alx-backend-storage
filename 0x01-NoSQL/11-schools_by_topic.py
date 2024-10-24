#!/usr/bin/env python3
"""
11. Where can I learn Python module
"""

def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of school
    """
    topic_filter = {
            'topics': {
                '$elemMatch': {
                    '$eq': topic,
                    },
                },
            }
    return [doc for doc in mongo_collection.find(topic_filter)]
