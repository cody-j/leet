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

def print_head(head):
    t = []
    n = head
    while n:
        t.append(n.val)
        n = n.next
    return t

def reverseNodesInGroup(head, k):
    n = head
    s = []
    l = 1

    print(print_head(head))
    while n:
        s.append(n)
        n = n.next
    dummy = Node() ## final bit
    while len(s) % k != 0:
        n = s.pop()
        n.next = dummy.next
        dummy.next = n

    print([x.val for x in s])

    remainder = dummy.next # pointer to the right side (processed) of the linked list
    next_head = None
    while s:
        rolling=len(s)%k==0
        will_roll=(len(s)-1)%k==0
        print('')

        node = s.pop()
        print(f'{node.val}{':rolling' if rolling else ''}{':will_roll' if will_roll else ''}')
        if not rolling and not will_roll:
            print('reversing')
        print(f'stack', [x.val for x in s])
        print("remainder pre:  ", print_head(remainder))
        if len(s) < 1:
            node.next = remainder
            remainder = next_head
            continue
        if len(s) > 0 and rolling:

            next_head = node
            node.next = s[-1]

        elif  len(s) > 0 and will_roll: # reversing
            node.next = remainder
            remainder = next_head
            s[-1].next = next_head
        else:
            node.next = s[-1]
            s[-1].next = None


        print("remainder post: ", print_head(remainder))

    print('')
    return remainder

if __name__=="__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)

    headr = reverseNodesInGroup(head, 2)

    h = headr
    f = []
    while h:
        f.append(h.val)
        h = h.next
    print(f)

