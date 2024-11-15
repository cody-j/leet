from collections import deque, defaultdict

def topological(graph, start):
    q = deque([start])
    seen = set(q)

    results = []
    while q:
        n = q.popleft()
        results.append(n)
        for v in graph[n]:
            if v not in seen:
                q.append(v)
                seen.add(v)

    return results

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

    print(topological(graph, 'A'))
