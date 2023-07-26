#!/usr/bin/python3
"""Implement a class MRUCache to cache by most recently used policy"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """Impliment a most recently used cache system"""

    def __init__(self):
        """Initialize a MRU cache"""
        self.keys = []
        self.indices = {}
        super().__init__()

    def put(self, key, item):
        """Insert a new item in the cache"""
        maxim = BaseCaching.MAX_ITEMS
        if key is None or item is None:
            return
        if len(self.cache_data) >= maxim and key not in self.keys:
            removable_key = self.keys.pop()
            self.indices.pop(removable_key)
            self.cache_data.pop(removable_key)
            print("DISCARD: {}".format(removable_key))

        self.cache_data[key] = item
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
            # We now update indices that fall behind the removed item
            affected = self.keys[index:]
            for k in affected:
                self.indices[k] = self.indices.get(k) - 1
            self.indices[key] = len(self.keys)
            self.keys.append(item)
            return value
        except KeyError:
            return None
