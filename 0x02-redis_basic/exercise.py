#!/usr/bin/env python3
"""
Writing strings to Redis
"""

import redis
from typing import Union
import uuid


class Cache:
    """
    A redis client class
    """
    def __init__(self):
        """Initializing class variable"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Return data in string format"""
        self.key = str(uuid.uuid4())
        self._redis.set(self.key, data)

        return self.key
