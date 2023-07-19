#!/usr/bin/env python3
"""
Redis
"""
import redis
from uuid import uuid4, UUID
from typing import Union, Optional, Callable


class Cache:
    """implementing cache class"""

    def __init__(self):
        """constructor method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store input data in redis by use of random key rtn key"""
        randomkey = str(uuid4())
        self._redis.set(randomkey, data)

        return randomkey 