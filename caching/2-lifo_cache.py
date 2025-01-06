#!/usr/bin/env python3
"""Module to implement LIFO Caching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Class LIFOCaching"""
    def __init__(self):
        """
        Constructor for class LIFOCaching
        """
        super().__init__()

    def put(self, key, item):
        """
        Assign value to given key for caching
        and delete the last item cached if number of items > MAX_ITEMS

        Args:
            keys (str): Name of the Cache key.
            item (any): Value to be cached.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key = list(self.cache_data.keys())[-1]
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve the cached value of given key

        Args:
            key (str): Name of cached key.

        Returns:
            any: Value of cached item.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
