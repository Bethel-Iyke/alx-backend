#!/usr/bin/env python3
"""Class that inherits from basechaching and a caching
   system using two different methods
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """The class LRUCache that inherit BaseCaching"""
    def __init__(self):
        """the initialization function that calls the parent class"""
        super().__init__()
        self.cache_item_order_list = []

    def put(self, key, item):
        """the put method that accepts two arguments,
        assigns value to the dictionary key """
        if key and item:
            if key in self.cache_data:
                self.cache_item_order_list.remove(key)
                self.cache_data[key] = item
                self.cache_item_order_list.append(key)
            if len(self.cache_data) < self.MAX_ITEMS:
                self.cache_item_order_list.append(key)
                self.cache_data[key] = item
            else:
                oldest_key = self.cache_item_order_list.pop(-1)
                del self.cache_data[oldest_key]
                self.cache_data[key] = item
                self.cache_item_order_list.append(key)
                print("DISCARD: {}".format(oldest_key))

    def get(self, key):
        """method that gets, takes two argument and return
        value in linked list"""
        if key is None and key not in self.cache_data:
            return None
        return self.cache_data[key]
