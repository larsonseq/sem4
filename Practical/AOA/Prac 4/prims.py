class PrimMST:
    def __init__(self, edges):
        # Initialize PrimMST object with edges
        self.edges = edges
        # Get unique vertices from edges
        self.vertices = {v for edge in edges for v in edge[:2]}
        # Print vertices for debugging
        print("IN init")
        print(self.vertices)
        # Number of vertices
        self.V = len(self.vertices)
        # Initialize MST
        self.mst = []

    def generate_mst(self):
        # Initialize visited, key, and parent dictionaries
        visited = {v: False for v in self.vertices}
        key = {v: float('inf') for v in self.vertices}
        parent = {v: None for v in self.vertices}

        # Start from vertex 0
        key[next(iter(self.vertices))] = 0

        # Iterate through vertices
        for _ in range(self.V):
            # Find the vertex with the minimum key value 
            u = min((v for v in self.vertices if not visited[v]), key=lambda v: key[v])
            # Mark u as visited
            visited[u] = True
            # Update key and parent for adjacent vertices of u
            for edge_u, v, w in self.edges:
                if edge_u == u and not visited[v] and w < key[v]:
                    key[v] = w
                    parent[v] = u

        # Store MST edges and their weights
        self.mst = [(parent[v], v, key[v]) for v in self.vertices if parent[v] is not None]
        return self.mst



# User input for edges and weights
def get_edges():
    num_edges = int(input("Enter the number of edges: "))
    edges = []
    for _ in range(num_edges):
        edge_input = input(f"Enter edge and weight for edge {_ + 1} (u,v,w): ").strip()
        # Split the input string by comma
        u, v, w = map(int, edge_input.split())
        edges.append((u, v, w))
    print(edges)
    return edges


# Main function
if __name__ == "__main__":
    # Get user input for edges and weights
    edges = get_edges()
    # Create PrimMST object with edges
    mst = PrimMST(edges)
    # Generate MST
    mst_edges = mst.generate_mst()
    # Calculate total cost of MST
    total_cost = sum(edge[2] for edge in mst_edges)

    # Print MST edges and their weights
    print("Minimum Spanning Tree Edges:")
    for edge in mst_edges:
        print(f"{edge[0]} - {edge[1]} : {edge[2]}")
    # Print total cost of MST
    print(f"Minimum Spanning Tree Cost: {total_cost}")
