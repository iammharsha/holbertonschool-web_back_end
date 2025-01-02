#!/usr/bin/env python3
"""Module to find documents by topic"""


def schools_by_topic(mongo_collection, topic):
    """
    Find and return the list of school having a specific topic

    Args:
        mongo_collection (Collection): A pymongo collection object.
        topic (str): List of topics approached in the school.
    """
    documents = mongo_collection.find({"topics": topic})
    return list(documents)
