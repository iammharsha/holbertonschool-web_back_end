#!/usr/bin/env python3
"""Module to list all documents in MongoDB collection"""


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    Args:
        mongo_collection: A pymongo collection object.

    Returns:
        A list of documents in the collection.
        Returns an empty list if the collection is empty.
    """
    if mongo_collection is None:
        return []

    return list(mongo_collection.find())
