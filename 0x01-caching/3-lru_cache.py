#!/usr/bin/python3
"""Implement a class LRUCache to cache by least recently used policy"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """Impliment a least recently used cache system"""

    def __init__(self):
        """Initialize an LRU cache"""
        self.keys = []
        self.indices = {}
        super().__init__()

    def put(self, key, item):
        """Insert a new item in the cache"""
        maxim = BaseCaching.MAX_ITEMS
        if key is None or item is None:
            return
        if len(self.cache_data) >= maxim and key not in self.keys:
            removable_key = self.keys.pop(0)
            self.indices.pop(removable_key)
            self.cache_data.pop(removable_key)
            self.update_values(self.indices, -1)
            print("DISCARD: {}".format(removable_key))

        self.cache_data[key] = item
        self.update_values(self.indices, -1)
        if key in self.keys:
            # First remove the existing key in the keys array if any
            item = self.keys.pop(self.indices.get(key))
        self.indices[key] = len(self.keys)
        self.keys.append(key)

    def get(self, key):
        """Retrieve an item from the cache, as well as update it's recency
        """
        try:
            value = self.cache_data[key]
            index = self.indices[key]
            item = self.keys.pop(index)
            self.update_values(self.indices, -1)
            self.indices[key] = len(self.keys)
            self.keys.append(item)
            return value
        except KeyError:
            return None

    def update_values(self, iterable, factor):
        """Update the numeric value of a dictionary iterable"""
        for k, v in iterable.items():
            iterable[k] = v + factor
