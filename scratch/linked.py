class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node(None)

    def append(self, val):
        nn = Node(val)
        n = self.head
        while n.next:
            n = n.next

        n.next = nn

    def prepend(self, key, val):
        nn = Node(key, val)
        nn.next = self.head.next
        self.head.next = nn

    def print_follow(self):
        n = self.head.next
        while n:
            print(n.val)
            print('-->')
            n = n.next


def reverse(n):
    if not n or not n.next:
        return n
    else:
        q = reverse(n.next)
        n.next.next = n
        n.next = None
        return q


if __name__=="__main__":
    l = LinkedList()
    l.append(1)
    l.append(2)
    l.append(3)

    l.head.next = reverse(l.head.next)
    l.print_follow()

