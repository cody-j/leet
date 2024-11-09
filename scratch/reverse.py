class Node:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next


def print_follow(head):
    n = head
    while n and n.next:
        print(n.val)
        n = n.next
    print(n.val)

def reverse(node):
    if not node or not node.next:
        return node
    q = reverse(node.next)
    node.next.next = node
    node.next = None
    return q


if __name__=="__main__":
    head = Node(0)
    head.next = Node(1)
    head.next.next = Node(2)
    print_follow(head)
    head = reverse(head)
    print_follow(head)
