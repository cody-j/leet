class Graph():
    def __init__(self):
        self.adj = {}

    def addNode(self, node):
        if node.key in self.adj:
            return
        self.adj[node] = []

    def addEdge(self, p, q):
        if p not in self.adj:
            return
        self.adj[p].append(q)

    def dfs(self):
        pass

    def bfs(self):
        pass

    def has_cycle(self):
        pass

    def __repr__(self):
        return str(self.adj)

class Node():
    def __init__(self, key, value):
        self.key, self.value = key, value

    def __hash__(self):
        return hash(self.key)

    def __repr__(self):
        return self.key



if __name__=="__main__":
    g = Graph()
    n = Node('A', 'Foo')
    m = Node('B', 'Bar')

    g.addNode(n)
    print(g)
    g.addNode(m)
    print(g)
    g.addEdge(n, m)
    g.addEdge(m, n)

    print(g)
    print(n)


