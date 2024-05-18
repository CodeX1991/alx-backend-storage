#!/usr/bin/env python3
"""Insert a document in Python"""


def insert_school(mongo_collection, **kwargs):
    """
    Args:
        mongo_collection: database collection
        kwargs: values to insert

    Return: the new _id
    """
    # Create an Insert object
    insert_obj = kwargs
    result = mongo_collection.insert_one(insert_obj)

    return result.inserted_id
