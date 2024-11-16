class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse(node):

    if node.next is None:
        return node

    tail = reverse(node.next)
    node.next.next = node
    node.next = None
    return tail


if __name__=="__main__":
    root = Node(1)
    root.next = Node(2)
    root.next.next = Node(3)
    root.next.next.next = Node(4)
    print(root.val)
    root = reverse(root)
    print(root.val)
