#!/usr/bin/env python3
"""Module to implement LRU Caching"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """Class LRUCaching"""
    def __init__(self):
        """
        Constructor for class LRUCaching
        """
        super().__init__()
        self.lru = OrderedDict()

    def put(self, key, item):
        """
        Assign value to given key for caching
        and delete the least recently used item cached
        if number of items > MAX_ITEMS

        Args:
            keys (str): Name of the Cache key.
            item (any): Value to be cached.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.lru.move_to_end(key)
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_used = next(iter(self.lru))
                self.cache_data.pop(last_used)
                self.lru.pop(last_used)
                print(f"DISCARD: {last_used}")
            self.cache_data[key] = item
            self.lru[key] = None

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
        self.lru.move_to_end(key)
        return self.cache_data[key]
