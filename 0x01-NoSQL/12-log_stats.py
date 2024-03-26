#!/usr/bin/env python3
""" nginx logs script"""
from pymongo import MongoClient


if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    doc_nbr = nginx_collection.count_documents({})
    print('{} logs'.format(doc_nbr))
    print('Methods:')
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        method_count = nginx_collection.count_documents({'method': method})
        print("    method {}: {}".format(method, method_count))
    number_doc = nginx_collection.count_documents({'method': "GET",
                                                   "path": "/status"})
    print('{} status check'.format(number_doc))
