#!/usr/bin/env python3
""" 8-all """


def list_all(mongo_collection):
    """list all document"""
    return [result for result in mongo_collection.find()]
