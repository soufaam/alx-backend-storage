#!/usr/bin/env python3
""" insert_school """


def schools_by_topic(mongo_collection, topic):
    """update"""
    return [result for result in mongo_collection.find(
                                        {'topics': topic})]
