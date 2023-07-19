#!/usr/bin/env python3
"""
Redis
"""
import redis
from uuid import uuid4, UUID
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """decorator counting how many times a func has been called"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ wrapper decorator func"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """decorator stores history of I/Oputs for partclr func"""
    
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper decor func"""
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)

        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)

        return output

    return wrapper

class Cache:
    """implementing cache class"""

    def __init__(self):
        """constructor method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store input data in redis by use of random key rtn key"""
        randomkey = str(uuid4())
        self._redis.set(randomkey, data)

        return randomkey 

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """reading from redis, convert to recover original type"""
        val = self._redis.get(key)
        if fn:
            val = fn(val)

        return val

    def get_str(self, key: str) -> str:
        """parameterizing a value from redis to string"""
        val = self._redis.get(key)
        return val.decode("utf-8")

    def get_int(self, key: str) -> int:
        """parameterizing a value from redis to string"""
        val = self._redis.get(key)
        try:
            val = int(val.decode("utf-8"))
        except Exception:
            val = 0
        return val
