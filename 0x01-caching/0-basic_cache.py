#!/usr/bin/python3
""" Defines BasicCache class """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ A caching system """

    def put(self, key, item):
        """ Inserts values to cache """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Retrives data from our cache """
        return self.cache_data.get(key, None)
