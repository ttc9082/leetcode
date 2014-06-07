import collections
class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.c = capacity
        self.d = collections.OrderedDict()
        self.n = 0

    # @return an integer
    def get(self, key):
        try:
            res = self.d[key]
            del self.d[key]
            self.d[key] = res
        except:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        try:
            del self.d[key]
            self.d[key] = value
            return
        except:
            if self.n == self.c:
                self.d.popitem(last=False)
                self.n -= 1
            self.n += 1
            self.d[key] = value
        return
                