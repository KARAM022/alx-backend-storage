#!/usr/bin/env python3
'''CMNT CMNT
'''


def update_topics(mongo_collection, name, topics):
    '''CMNT CMNT
    '''
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
