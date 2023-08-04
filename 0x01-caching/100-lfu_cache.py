#!/usr/bin/env python3
""" Defines LFUCache """
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """ An LFU caching system """
    def __init__(self):
        """ Initializes the cache """
        super().__init__()
        self.cache_data = OrderedDict()
        self.keys_frequency = []

    def put(self, key, item):
        """ Adds an item to the cache """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lfu_key, _ = self.keys_frequency[-1]
                self.cache_data.pop(lfu_key)
                self.keys_frequency.pop()
                print("DISCARD:", lfu_key)
            self.cache_data[key] = item
            insert_index = len(self.keys_frequency)
            for i, key_freq in enumerate(self.keys_frequency):
                if key_freq[1] == 0:
                    insert_index = i
                    break
            self.keys_frequency.insert(insert_index, [key, 0])
        else:
            self.cache_data[key] = item
            self.__reorder_items(key)

    def get(self, key):
        """Retrieves data from the cache """
        if key is not None and key in self.cache_data:
            self.__reorder_items(key)
        return self.cache_data.get(key, None)

    def __reorder_items(self, mru_key):
        """ reorders items in the cache based on usage (MRU) """
        max_positions = []
        mru_frequency = 0
        mru_position = 0
        position_inserted = 0
        for i, key_freq in enumerate(self.keys_frequency):
            if key_freq[0] == mru_key:
                mru_frequency = key_freq[1] + 1
                mru_position = i
                break
            elif len(max_positions) == 0:
                max_positions.append(i)
            elif key_freq[1] < self.keys_frequency[max_positions[-1]][1]:
                max_positions.append(i)
        max_positions.reverse()
        for pos in max_positions:
            if self.keys_frequency[pos][1] > mru_frequency:
                break
            position_inserted = pos
        self.keys_frequency.pop(mru_position)
        self.keys_frequency.insert(position_inserted, [mru_key, mru_frequency])
