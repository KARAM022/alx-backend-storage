#!/usr/bin/env python3
'''CMNT CMNT
'''


def list_all(mongo_collection):
    '''CMNT CMNT
    '''
    return [doc for doc in mongo_collection.find()]
