#!/usr/bin/env python3
"""Module to Insert School to MongoDB Collection"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a MongoDB collection.

    Args:
        mongo_collection: A pymongo collection object.
        **kwargs: Key-value pairs representing the fields of the document.

    Returns:
        The _id of the inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    
    return result.inserted_id
