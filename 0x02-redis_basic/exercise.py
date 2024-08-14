#!/usr/bin/env python3
""" Redis exercise """


import redis
import uuid
from typing import Union


class Cache:
    """ Cache class """
    def __init__(self):
        """ Initialize Cache class """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store data in Redis """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn=None) -> Union[str, bytes, int, float]:
        """ Get data from Redis """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data
    
    def get_str(self, key: str) -> str:
        """ Get data from Redis as string """
        return self.get(key, str)
    
    def get_int(self, key: str) -> int:
        """ Get data from Redis as int """
        return self.get(key, int)
