
class LRU:
    def __init__(self, capacity=10):
        self.capacity = capacity
        # implement some linked list-based cache

    def put(self):
        pass

    def get(self):
        pass

    def __repr__(self):
        return 'lru cache!'

    def __len__(self):
        return self.capacity

if __name__=="__main__":
    cache = LRU()
    print(cache)
    print(len(cache))
