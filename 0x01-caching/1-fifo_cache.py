#!/usr/bin/env python3
""" Class that inherits from BaseCaching and is a caching system """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """class called fifocache that inherits from basecaching"""

    def __init__(self):
        """initilization class instance
        """
        super().__init__()
        self.cache_item_order_list = []

    def put(self, key, item):
        """the put method that assign to the dictionary key item value."""
        if key and item:
            self.cache_data[key] = item
            """add item value to the self.cache.data"""
            self.cache_item_order_list.append(key)
            """appends key to the self data list"""
            if len(self.cache_data) > self.MAX_ITEMS:
                """checks if line exceeds the number of items allowed"""
                self.cache_data.pop(self.cache_item_order_list[0])
                """removes the older item and assign it to a variable"""
                old_key_list = self.cache_item_order_list.pop(0)
                print("DISCARD: {}".format(old_key_list))

    def get(self, key):
        """get method that returns key of data in cache if present"""
        if key in self.cache_data:
            """checks if key is present in data cache list"""
            return self.cache_data[key]
        else:
            return None
