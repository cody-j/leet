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

if __name__=="__main__":
    l = LinkedList()
    l.append(Node(1))
    l.append(Node(2))
    l.append(Node(3))
    l.print_follow()
