from collections import OrderedDict
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.h = OrderedDict()

    def get(self, key):
        if key not in self.h:
            return -1
        value = self.h.pop(key)         # Remove the key
        self.h[key] = value             # Reinsert it to mark as recently used
        return value

    def put(self, key, value):
        if key in self.h:
            self.h.pop(key)
            self.h[key] = value
        
        elif len(self.h )>= (self.cap ):
            for i in self.h:
                self.h.pop(i)
                break
            self.h[key] = value
        else:
            self.h[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)