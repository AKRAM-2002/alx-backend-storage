#!/usr/bin/env python3
"""
Redis & Python
"""
import uuid
import redis
from typing import Union, Callable, Optional
import functools

def count_calls(method: Callable) -> Callable:
        """Decorator to count calls to a method."""
            @functools.wraps(method)
            def wrapper(self, *args, **kwargs):
                key = method.__qualname__  
                self._redis.incr(key)
                return method(self, *args, **kwargs)  
            return wrapper

def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs and outputs for a function."""
      @functools.wraps(method)
       def wrapper(self, *args, **kwargs):
            inputs_key = f"{method.__qualname__}:inputs"
            outputs_key = f"{method.__qualname__}:outputs"
            self._redis.rpush(inputs_key, str(args))
            output = method(self, *args, **kwargs)
            self._redis.rpush(outputs_key, output)
            return output
        return wrapper


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

    @count_calls
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

    def get(self,key: str, fn: Optional[Callable] = None) -> Union[str,bytes,int, float,None]:
        '''
        Retrieve data from Redis and apply an optional conversion function
        '''
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, fn: Callable):
        """Retrieve a string value from Redis."""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, fn: Callable):
        """Retrieve an integer value from Redis."""
        return self.get(key, fn=int)
