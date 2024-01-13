#!/usr/bin/env python3
"""
Write a Python function that changes all topics of a school document based on the name:
    Prototype: def update_topics(mongo_collection, name, topics):
    mongo_collection will be the pymongo collection object
    name (string) will be the school name to update
    topics (list of strings) will be the list of topics approached in the school
"""


def update_topics(mongo_collection, name, topics):
    """
    Update topics of a school document in MongoDB.

    Args:
        mongo_collection: pymongo collection object.
        name (str): School name to update.
        topics (list of str): List of topics approached in the school.
    """
    query = {"name": name}
    update_data = {"$set": {"topics": topics}}
    mongo_collection.update_one(query, update_data)
