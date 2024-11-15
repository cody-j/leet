from collections import deque, defaultdict

def topological(graph):
    """
    The main difference between topological sort and bfs in in queueing choice, and state tracking,
    particularly adding not all neighbours, but only those with a zero in_degree (after current
    node processed and decrements its neighbours).
    """
    in_degree = defaultdict(int)
    for node in graph:
        for neighbour in graph[node]:
            in_degree[neighbour] += 1
    print(f'in degree: {in_degree}')
    q = deque([node for node in graph if in_degree[node] == 0])



    results = []
    while q:
        n = q.popleft()
        results.append(n)
        for neighbour in graph[n]:
            in_degree[neighbour] -= 1
            if in_degree[neighbour] == 0:
                q.append(neighbour)

    if len(results) != len(graph):
        return None # cycle detected
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

    print(topological(graph))
