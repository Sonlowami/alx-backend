#!/usr/bin/python3
"""Implement a class LRUCache to cache by least recently used policy"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """Impliment a least recently used cache system"""

    def __init__(self):
        """Initialize an LRU cache"""
        self.keys = []
        super().__init__()

    def put(self, key, item):
        """Insert a new item in the cache"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCashing.MAX_ITEMS and key not in self.keys:
            removable_key = self.keys.pop[0]
            self.cache_data.pop(key)
            print("DISCARD: {}".format(key))
        self.cache_data[key] = item
        self.keys.append(key)
