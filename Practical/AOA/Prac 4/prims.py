class PrimMST:
    def __init__(self, edges):
        self.edges = edges
        self.vertices = set().union(*edges)
        print(self.vertices)
        self.V = len(self.vertices)
        self.mst = []

    def generate_mst(self):
        visited = {v: False for v in self.vertices}
        key = {v: float('inf') for v in self.vertices}
        parent = {v: None for v in self.vertices}

        # Start from vertex 0
        key[next(iter(self.vertices))] = 0

        for _ in range(self.V):
            u = min((v for v in self.vertices if not visited[v]), key=lambda v: key[v])
            visited[u] = True
            for v, w in self.edges:
                if u in (v, v) and not visited[v] and w < key[v]:
                    key[v] = w
                    parent[v] = u

        self.mst = [(parent[v], v, key[v]) for v in self.vertices if parent[v] is not None]
        return self.mst


# User input
def get_edges():
    num_edges = int(input("Enter the number of edges: "))
    edges = []
    for _ in range(num_edges):
        edge_input = input(f"Enter edge and weight for edge {_ + 1} (u,v,w): ").strip()
        u, v, w = map(int, edge_input.split(','))
        edges.append((u, v, w))
    return edges


# Main function
if __name__ == "__main__":
    edges = get_edges()
    mst = PrimMST(edges)
    mst_edges = mst.generate_mst()
    total_cost = sum(edge[2] for edge in mst_edges)

    print("Minimum Spanning Tree Edges:")
    for edge in mst_edges:
        print(f"{edge[0]} - {edge[1]} : {edge[2]}")
    print(f"Minimum Spanning Tree Cost: {total_cost}")
