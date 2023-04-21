#!/usr/bin/env python3
"""Class that inherits from basecaching and is a caching system that,
assign value to dictionary keys """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """class that inherits basecaching"""

    def __init__(self):
        """class init instance calling parent class"""
        super().__init__()
        self.data = []

    def put(self, key, item):
        """the put method that takes in two arguments and deletes the most
        recent data which is usually at the beginning of the array"""
        if key and item:
            self.cache_data[key] = item
        if key not in self.data:
            self.data.append(key)
        else:
            self.data.remove(key)
            self.data.append(key)
        if len(self.data) > BaseCaching.MAX_ITEMS:
            mru = self.data.pop(-2)
            del self.cache_data[mru]
            print("DISCARD: {}".format(mru))

    def get(self, key):
        """ the get method that return the value of the
        dictionary key linked to it """
        if key:
            if key in self.cache_data:
                self.data.remove(key)
                self.data.append(key)
                return self.cache_data[key]
            return None
