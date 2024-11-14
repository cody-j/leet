import heapq

def dfs(graph, start):
    pass


def shortest_path(graph, start, end):
    # lowest seen distance to start node (initialized as inifitely long)
    distances = {node: float('inf') for node in graph}

    distances[start] = 0

    # tracked path adjacency list (?)
    previous = {node: None for node in graph}

    # priority queue as built-in heapq min-heap
    # heapq.heappush
    # heapq.heappop
    pq = [(0, start)]

    while pq:
        print(pq)
        d, v = heapq.heappop(pq)
        if v == end:
            break

        if d > distances[v]:
            continue

        for vn, dn in graph[v]:
            distance = d + dn
            if distance < distances[vn]:
                distances[vn] = distance
                previous[vn] = v
                heapq.heappush(pq, (dn, vn))






if __name__=="__main__":
    graph = {
        'A': [('C', 2), ('A', 1)],
        'B': [('C', 1), ('D', 5)],
        'C': [('A', 2), ('D', 8), ('B', 1) ],
        'D': [('B', 5), ('C', 8)]
    }

    result = shortest_path(graph, 'A', 'D')
    print(result)
