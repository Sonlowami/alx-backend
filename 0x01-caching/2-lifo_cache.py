#!/usr/bin/env python3
"""Contain LIFOCache, a class that implements a LIFO cache structure"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Implement a LIFO cache structure based on the structure defined in
    BaseCaching. The data structure to hold our cache data will be in
    self.cache_data
    """

    def __init__(self):
        """Initialize a cache object"""
        self.keys = []
        super().__init__()

    def put(self, key, item):
        """Add a new item to the cache"""
        maxim = BaseCaching.MAX_ITEMS
        if key is None and item is None:
            return
        if len(self.cache_data) >= maxim and key not in self.keys:
            removable_key = self.keys.pop()
            self.cache_data.pop(removable_key)
            print("DISCARD: {}".format(removable_key))

        self.cache_data[key] = item
        self.keys.append(key)

    def get(self, key):
        """Retrieve a value from the cache"""
        try:
            return self.cache_data[key]
        except KeyError:
            return None
