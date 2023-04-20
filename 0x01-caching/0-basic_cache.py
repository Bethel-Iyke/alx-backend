#!/usr/bin/env python3
""" Create a class that inherits and is a caching system """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ class that inherits from BaseCaching """

    def __init__(self):
        """class initialization instance"""
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """defines the put method and returns nothing if key or item is none"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """defines the get method and returns data linked to the key"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
