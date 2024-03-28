#!/usr/bin/env python3
"""Writing strings to Redis"""
from redis import Redis
from typing import Union, Callable
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """doc doc class"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)


class Cache:
    """Class Cache"""
    def __init__(self):
        """init method"""
        self._redis = Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """return string"""
        rkey = str(uuid.uuid4())
        self._redis.set(rkey, data)
        return rkey

    def get(self, key: str, fn: Union[Callable, type(None)] = None):
        """A method convert to fn"""
        if not key:
            value = self._redis.get(key)
        elif fn:
            value = fn(self._redis.get(key))
        else:
            value = self._redis.get(key)
        return value

    def get_str(self, key: str):
        """get_str"""
        return self.get(key, str)

    def get_int(self, key):
        """get_str"""
        return self.get(key, int)
