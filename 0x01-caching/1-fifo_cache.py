#!/usr/bin/env python3
"""FIFOCache that inherits from BaseCaching and is a caching system
"""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCaching defines:
      - inherits from BaseCaching and is a caching system
      - where your data are stored (in a dictionary)
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if len(self.cache_data) < BaseCaching.MAX_ITEMS:
                self.cache_data[key] = item
            else:
                self.cache_data[key] = item
                keys = list(self.cache_data.keys())
                print("DISCARD: {}".format(keys[0]))
                del self.cache_data[keys[0]]

    def get(self, key):
        """ Get an item by key
        """
        if not key or not self.cache_data.get(key):
            return None
        return self.cache_data.get(key)
