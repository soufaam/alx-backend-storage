#!/usr/bin/env python3
""" insert_school """


def update_topics(mongo_collection, name, topics):
    """update"""
    return mongo_collection.update_many({"name": name},
                                        {'$set': {'topics': topics}})
