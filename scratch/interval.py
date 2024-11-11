# Node
class Node:
    def __init__(self, interval):
        self.interval = interval
        self.max_end = interval[1]
        self.left = None
        self.right = None

# IntervalTree
class IntervalTree:
    def __init__(self):
        self.root = None

    def insert(self, interval):
        def _insert(node, interval):
            if not node:
                return Node(interval)
            node.max_end = max(node.max_end, interval[1])
            if interval[0] < node.interval[0]:
                node.left = _insert(node.left, interval)
            else:
                node.right = _insert(node.right, interval)
            return node

        self.root = _insert(self.root, interval)

    def print_follow(self):
        def _print(node):
            if not node:
                return
            if node.left is not None:
                _print(node.left)

            print(node.max_end, node.interval)

            if node.right is not None:
                _print(node.right)

        _print(self.root)

if __name__=="__main__":
    intervals = IntervalTree()
    intervals.insert([1, 4])
    intervals.insert([2, 6])
    intervals.insert([4, 10])
    intervals.insert([0, 3])

    intervals.print_follow()
