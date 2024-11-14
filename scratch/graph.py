
def bfs(graph, start):
    horizon = [start]
    seen = set(horizon)

    while horizon:
        node = horizon.pop(0)

        for neighbour, d in graph[node]:
            if neighbour not in seen:
                horizon.append(neighbour)
                seen.add(neighbour)



    return seen

def dfs(graph, start):

    def _dfs(start, seen=None):
        pass


