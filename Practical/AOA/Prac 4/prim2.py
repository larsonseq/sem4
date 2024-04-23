class PrimsMST():
    def __init__(self, edges):
        self.edges = edges
        self.vertices = {v for edge in edges for v in edge[:2]}
        print(self.vertices)
        self.V = len(self.vertices)
        self.mst = []

    def generate_mst(self):
        visited = {v:False for v in self.vertices}
        key = {v : float('inf') for v in self.vertices}
        parent = {v: None for v in self.vertices}

        key[next(iter(self.vertices))] = 0

        for j in range(self.V):
            u = min((v for v in self.vertices if not visited[v]), key = lambda v : key[v])
            visited[u] = True

            for edge_u, v, w in self.edges:
                if edge_u == u and not visited[v] and w < key[v]:
                    key[v] = w
                    parent[v] = u
            
        self.mst = [(parent[v], v, key[v]) for v in self.vertices if parent[v] is not None]
        return self.mst



def getEdges():
    n = int(input("Enter number of edges :"))
    edges = []
    for i in range(n):
        edge = tuple(map(int, input(f"Enter edges for { i + 1}").split()))
        edges.append(edge)
    return edges

if __name__ =="__main__":
    edges = getEdges()
    print(edges)
    mst = PrimsMST(edges)
    mst_edges = mst.generate_mst()
    totalcost = sum(edge[2] for edge in mst_edges)
    print(totalcost)