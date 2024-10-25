#!/usr/bin/env python3
"""
Redis & Python
"""
import uuid
import redis
from typing import Union


class Cache:
    """
    Class Cache
    """

    def __init__(self):
        """
        Inialize Redis Client and flush the database
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis with a random key.

        Args:
            data: The data to be stored, which can be of
            type str, bytes, int, or float.
        Returns:
            str: The generated random key used to store the data in Redis.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
