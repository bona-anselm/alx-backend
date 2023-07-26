#!/usr/bin/python3
""" Defines class BasicCache """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ A caching system """
    def put(self, key, item):
        """ Inserts data into our dictionary """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        return self.cache_data.get(key, None)
