'''
Link+
'''
class Item:
    def __init__(self, key=None, val=None):
        self.key, self.val = key, val
        self.next = self.prev = None
    
    def __repr__(self):
        return str(self.val)


'''
Implementation of LRU Cache (Least Recent Usage)
LinkedList+
'''
class Cache:

    def __init__(self, max_size=4):
        # Initialize head and tail; left / right
        self.left = Item(key=None, val=None)
        self.right = Item(key=None, val=None)
        self.left.next, self.right.prev = self.right, self.left
        
        self.max_size = max_size
        self.cache = {} # key: Item
        self.size = 0 

    def insert_at_front(self, node):
        node.prev = self.right.prev
        node.next = self.right
        self.right.prev.next = self.right.prev = node
        
        return node
    
    def remove(self, node):
        if node.key in self.cache:
            node.prev.next, node.next.prev = node.next, node.prev
            self.size -= 1
            return node

    def put(self, k, v):
        if k in self.cache:
            self.cache[k].val = v
            self.insert_at_front(self.remove(self.cache[k]))
        else:
            if self.size == self.max_size:
                self.remove(self.left.next)

            self.cache[k] = Item(k, v)
            self.insert_at_front(self.cache[k])
            self.size += 1
        
        pass

    def clear(self):
        self.cache = {}
        self.left.next, self.right.prev = self.right, self.left

    
    
    def __repr__(self):
        nodes = []

        n = self.left.next
        while n:
            nodes.append(n)
            n = n.next

        return ' '.join([str(n.val) for n in nodes[:-1]])

    def __len__(self): 
        return self.size



if __name__=="__main__":
    cache = Cache(max_size=4)

    print(cache)

    cache.put("first", "1")
    cache.put("second", "2")
    cache.put("third", "3")
    cache.put("fourth", "4")

    print(cache)

    cache.put("fifth", "5")
    print(len(cache))
    cache.put("second", "20")
    cache.put("third", "30")
    cache.put("fourth", "4")
    print(cache)

    cache.clear()

    cache.put("first", "1")
    cache.put("second", "2")
    print(cache)
