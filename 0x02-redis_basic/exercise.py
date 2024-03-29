#!/usr/bin/env python3
"""Writing strings to Redis"""
import redis
from typing import Union, Callable, Optional
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
    return wrapper


def replay(method: Callable) -> None:
    """doc doc class"""
    input_key = "{}:inputs".format(method.__qualname__)
    output_key = "{}:outputs".format(method.__qualname__)

    inputs = method.__self__._redis.lrange(input_key, 0, -1)
    outputs = method.__self__._redis.lrange(output_key, 0, -1)

    print("{} was called {} times:".format(method.__qualname__, len(inputs)))
    for inp, out in zip(inputs, outputs):
        print(
            "{}(*{}) -> {}".format(
                method.__qualname__, inp.decode("utf-8"), out.decode("utf-8")
            )
        )


def call_history(method: Callable) -> Callable:
    """doc doc class"""
    inkey = method.__qualname__ + ":inputs"
    outkey = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """doc doc class"""
        self._redis.rpush(inkey, str(args))
        res = method(self, *args, **kwargs)
        self._redis.rpush(outkey, str(res))
        return res

    return wrapper


class Cache:
    """Class Cache"""
    def __init__(self):
        """init method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """return string"""
        rkey = str(uuid.uuid4())
        self._redis.set(rkey, data)
        return rkey

    def get(
        self, key: str, fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float]:
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
