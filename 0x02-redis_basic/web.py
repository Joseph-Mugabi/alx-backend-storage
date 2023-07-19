#!/usr/bin/env python3
'''
implementing a module with tools, request caching and tracking
'''
import requests
import redis
from functools import wraps
from typing import Callable


redisstore = redis.Redis()
'''level Redis instance'''


def data_cacher(method: Callable) -> Callable:
    '''caches the output of fetched data.'''
    @wraps(method)
    def invoker(url) -> str:
        '''wrapper function for caching the output'''
        redisstore.incr(f'count:{url}')
        result = redisstore.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        result = method(url)
        redisstore.set(f'count:{url}', 0)
        redisstore.setex(f'result:{url}', 10, result)
        return result
    return invoker


@data_cacher
def get_page(url: str) -> str:
    '''returns the content of a url after caching the request's
    response & tracking the requests.'''
    return requests.get(url).text
