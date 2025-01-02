#!/usr/bin/env python3
"""Module to update MongoDB collection with given name"""


def update_topics(mongo_collection, name, topics):
    """
    Change all topics of a school document based on the name

    Args:
        mongo_collection (Collection): A pymongo collection object.
        name (str): School Name to be updated
        topics (List[str]): List of topics approached in the school

    Returns:
        None
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
