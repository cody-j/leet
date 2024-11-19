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



def search(graph):
    start = 'A'
    seen = set([start])
    results = [start]
    def dfs(graph, node):
        if not node:
            return
        for neighbour in reversed(graph[node]):
            if neighbour not in seen:
                results.append(neighbour)
                seen.add(neighbour)
                dfs(graph, neighbour)
    dfs(graph, start)
    return results


if __name__=="__main__":

    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'D', 'E'],
        'D': ['B', 'C', 'E'],
        'E': ['C', 'D']
    }

    print(search(graph))
    # root = Node(1)
    # root.next = Node(2)
    # root.next.next = Node(3)
    # root.next.next.next = Node(4)
    # print(root.val)
    # root = reverse(root)
    # print(root.val)
