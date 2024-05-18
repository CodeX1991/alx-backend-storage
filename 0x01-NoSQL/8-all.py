#!/usr/bin/env python3
"""List all docuuments in Python"""


def list_all(mongo_collection):
    """
    Args:
        mongo_collection: database collection

    Return: empty list if no document or list
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
