#!/usr/bin/env python3
"""Change school topics"""


def update_topics(mongo_collection, name, topics):
    """
    Args:
        mongo_collection: database collection
        name: school name to work with
        topics: list of strings
    """
    updateResult = mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}})
    return updateResult
