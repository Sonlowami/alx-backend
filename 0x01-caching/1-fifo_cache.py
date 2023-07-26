#!/usr/bin/env python3
"""Contain FIFOCache, a first-in first-out implimentation of a cache"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    Implement a first-in first out cache data structure
    """

    def __init__(self):
        """Initialize the cache object"""
        self.keys = []
        super().__init__()

    def put(self, key, item):
        """Add an item to our cache"""
        maxim = BaseCaching.MAX_ITEMS
        if key is None or item is None:
            return

        if len(self.cache_data) >= maxim and key not in self.keys:
            removable_key = self.keys.pop(0)
            self.cache_data.pop(removable_key)
            print("DISCARD: {}".format(removable_key))

        self.cache_data[key] = item
        self.keys.append(key)

    def get(self, key):
        """Retrieve an item from the cache"""
        try:
            return self.cache_data[key]
        except KeyError:
            return None
