#!/usr/bin/env python3
"""Class that inherits from BaseCaching and is a caching system. """


from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """class lifocache"""
    def __init__(self):
        """function that calls parent init"""
        super().__init__()
        self.cache_item_order_list = []

    def put(self, key, item):
        """the put method that takes two argument,
        add item value to the dictionary key"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            keys = list(reversed(list(self.cache_data.keys())))
            last_key = keys[0]
            del self.cache_data[last_key]
            print("DISCARD: {}".format(last_key))
        self.cache_data[key] = item

    def get(self, key):
        """method that gets item from the cache"""
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
