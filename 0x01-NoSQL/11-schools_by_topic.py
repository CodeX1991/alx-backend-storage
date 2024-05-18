#!/usr/bin/env python3
""" Returns the list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """
    Args:
        mongo_collection: database collections
        topics: a string
    """
    findResult = list(mongo_collection.find({"topics": topic}))
    return findResult
