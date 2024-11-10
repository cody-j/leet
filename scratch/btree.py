class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# preorder
def dfs(node=None):
    if node is None: return []
    return dfs(node.left) + [node.val] + dfs(node.right)

def bfs(node):
    pass

def max_depth(node):
    if node is None: return 0
    return 1 + max(max_depth(node.right), max_depth(node.left))

'''
            0
    1              4
2       3       5       6
'''
if __name__=="__main__":
    root = Node(0)

    root.left = Node(1)
    root.left.left = Node(2)
    root.left.right = Node(3)

    root.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)

    print(dfs(root))
    print(max_depth(root))
