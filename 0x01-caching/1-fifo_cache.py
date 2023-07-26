#!/usr/bin/python3
""" Defines FIFOCache """
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """ A FIFO caching system """
    def __init__(self):
        """ Initializes our cache """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Inserts values to cache """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """ Retrives data from our cache """
        return self.cache_data.get(key, None)
