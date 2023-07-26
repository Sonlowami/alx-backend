#!/usr/bin/env python3
"""Impliment a basic caching feature"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Implement a basic caching into a dictionary of limitless size"""

    def put(self, key, item):
        """Save an item to our caching dictionary on a key, key.
        If anything between key and item is a None value, the method
        does nothing
        """
        if key is None or item is None:
            return
        self.cache_data.update({key: item})

    def get(self, key):
        """Retrieve an item from our caching dictionary, given a key.
        If key is invalid or None, the method also returns None
        """
        try:
            return self.cache_data[key]
        except KeyError:
            return None
