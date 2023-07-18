#!/usr/bin/env python3
"""Module lists all documents in a collection"""


def list_all(mongo_collection):
    """lists all documents in a collection"""
    all_docus = []
    for docu in mongo_collection.find():
        all_docus.append(doc)
    return all_docus
