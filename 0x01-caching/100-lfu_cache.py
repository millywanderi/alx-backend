#!/usr/bin/env python3
"""LFUCache that inherits from BaseCaching and is a caching system
"""


from collections import OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCaching defines:
      - inherits from BaseCaching and is a caching system
      - where your data are stored (in a dictionary)
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.count = {}

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if len(self.cache_data) < BaseCaching.MAX_ITEMS:
                orderkeys = self.cache_data.keys()
                ordercount = self.count.keys()
                if key in self.cache_data:
                    self.cache_data[key] = item
                    self.count[key] += 1
                else:
                    self.cache_data[key] = item
                    self.count[key] = 1
                tkeys = [(key, self.cache_data[key]) for key in orderkeys]
                self.cache_data = OrderedDict(tkeys)
                tcount = [(key, self.count[key]) for key in ordercount]
                self.count = OrderedDict(tcount)
            else:
                if key not in self.cache_data:
                    minkey = min(self.count, key=self.count.get)
                    del self.count[minkey]
                    print("DISCARD: {}".format(minkey))
                    del self.cache_data[minkey]
                else:
                    self.cache_data[key] = item
                    self.count[key] += 1

    def get(self, key):
        """ Get an item by key
        """
        if not key or not self.cache_data.get(key):
            return None
        self.cache_data.move_to_end(key, last=True)
        self.count[key] += 1
        self.cache_data.move_to_end(key, last=True)
        return self.cache_data[key]
