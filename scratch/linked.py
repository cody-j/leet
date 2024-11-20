class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, node):
        n = self.head
        while n.next:
            n = n.next

        n.next = node

    def print_follow(self):
        n = self.head.next
        while n and n.next:
            print(n.val)
            n = n.next



def reverseNodesInGroup(head, k):
    n = head
    s = []
    l = 1

    while n:
        s.append(n)
        n = n.next

    print([x.val for x in s])
    t = s[-1]

    while s:
        if len(s) % k == 0:
            #reverse
            print([x.val for x in s])

        p = s.pop()
        if len(s) > 0:
            p.next = s[-1]
        else:
            p.next = None

    return t

if __name__=="__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    headr = reverseNodesInGroup(head, 2)
    print(headr.val)
    h = headr
    while h:
        print(h.val)
        h = h.next

