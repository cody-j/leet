from collections import deque, defaultdict

def topological(graph):
    deps = defaultdict(int)

    pass

if __name__=="__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['E', 'G'],
        'D': ['E'],
        'E': ['F'],
        'F': ['G'],
        'G': []
    }
    topological(graph)
