class LRU:

    def __init__(self, size):

        self.size = size
        self.cache = []

    def them(self, value):

        if value in self.cache:
            self.cache.remove(value)

        self.cache.append(value)

        if len(self.cache) > self.size:
            self.cache.pop(0)


lru = LRU(3)

lru.them(1)
lru.them(2)
lru.them(3)
lru.them(4)

print(lru.cache)