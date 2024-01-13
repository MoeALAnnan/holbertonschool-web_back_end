#!/usr/bin/env python3
"""
    Module
"""

import pymongo


def list_all(mongo_collection):
    """
    Function comment:
    This function takes a MongoDB collection and key-value pairs (**kwargs) as input,
    """
    return mongo_collection.find()
