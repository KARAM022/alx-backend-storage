#!/usr/bin/env python3
'''CMNT CMNT
'''


def insert_school(mongo_collection, **kwargs):
    '''CMNT CMNT
    '''
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
