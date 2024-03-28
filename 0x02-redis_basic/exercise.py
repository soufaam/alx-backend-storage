#!/usr/bin/env python3
"""Writing strings to Redis"""
from redis import Redis
from typing import Union
import uuid


class Cache:
    """Class Cashe"""
    def __init__(self):
        """init method"""
        self._redis = Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """return string"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
