#!/usr/bin/env python3
'''CMNT CMNT
'''


def schools_by_topic(mongo_collection, topic):
    '''CMNT CMNT
    '''
    topic_filter = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    return [doc for doc in mongo_collection.find(topic_filter)]
