#!/usr/bin/env python3
"""Module to implement MRU Caching"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """Class MRUCaching"""
    def __init__(self):
        """
        Constructor for class LRUCaching
        """
        super().__init__()
        self.mru = OrderedDict()

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
                self.cache_data[key] = item
                self.mru.move_to_end(key)
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                recently_used = next(iter(self.mru))
                self.cache_data.pop(recently_used)
                self.mru.pop(recently_used)
                print(f"DISCARD: {recently_used}")
            self.cache_data[key] = item
            self.mru[key] = None
            self.mru.move_to_end(key, False)

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
        self.mru.move_to_end(key, False)
        return self.cache_data[key]
