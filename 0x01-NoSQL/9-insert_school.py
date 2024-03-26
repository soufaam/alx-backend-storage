#!/usr/bin/env python3
""" insert_school """


def insert_school(mongo_collection, **kwargs):
    """insert_school"""
    return mongo_collection.insert_one(kwargs).inserted_id
