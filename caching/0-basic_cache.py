#!/usr/bin/env python3
"""Module to implement Basic Caching"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Class BasicCaching"""

    def put(self, key, item):
        """
        Assign cache value to given key in cache dictionary.

        Args:
            key (str): Name of the Cache key.
            item (any): Value to be cached
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve the cached value with given key.

        Args:
            key (str): Key of the cached value to retrieve
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
