class Node:
    def __init__(self, key, val=None):
        self.key, self.val = key, val
        self.next = None
        self.prev = None

# doubly linked
class LinkedHashMap:
    def __init__(self):
        self.hash_map = {}
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next, self.tail.prev = self.tail, self.head

    def __str__(self):
        return str(self.hash_map)

class LRU:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.cache = LinkedHashMap()

    def put(self):
        pass

    def get(self):
        pass

    def __len__(self):
        return self.capacity

    def __repr__(self):
        return str(self.cache)

if __name__=="__main__":
    cache = LRU()
    print(cache)
