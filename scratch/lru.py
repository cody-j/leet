class Node:
    def __init__(self, key, val=None):
        self.key, self.val = key, val
        self.next = None
        self.prev = None
    def __hash__(self):
        return hash(self.key)

# doubly linked
class LinkedHashMap:
    def __init__(self):
        self.hash_map = {}
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next, self.tail.prev = self.tail, self.head

    def add_to_tail(self, key, val):
        if key in self.hash_map:
            # cache hit
            n = self.hash_map[key]
            self._remove(n)
            self._append(n)
        else:
            # cache miss
            n = Node(key, val)
            self.hash_map[key] = n
            self._append(n)

    def get(self, key):
        if key in self.hash_map:
            return self.hash_map[key].val
        else:
            return -1

    def _append(self, node):
        node.next, node.prev = self.tail, self.tail.prev
        node.prev.next = node.next.prev = node

    def _remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def __str__(self):
        return str(self.hash_map)

    def print_follow(self):
        n = self.head.next
        while n.next:
            print(n.key)
            n = n.next

    def __len__(self):
        return len(self.hash_map)

class LRU:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.items = LinkedHashMap()

    def put(self, key, val):
        self.items.add_to_tail(key, val)

    def get(self, key):
        return self.items.get(key)

    def __len__(self):
        return self.capacity

    def __repr__(self):
        return str(self.items)

if __name__=="__main__":
    cache = LRU()
    cache.put('foo', '1')
    cache.put('bar', '2')
    cache.items.print_follow()
    cache.put('baz', '3')
    cache.items.print_follow()
    print(cache.get('asdf'))
