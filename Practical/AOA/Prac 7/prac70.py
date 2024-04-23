def input_graph():
    """
    Function to take user input for graph.
    """
    global n, count
    n = int(input("Enter the number of vertices in the graph: "))
    graph = [[0] * n for _ in range(n)]
    vertices = [None] * n
    print("Enter the adjacency matrix of the graph (separate elements by space):")
    for i in range(n):
        graph[i] = list(map(int, input().split()))
    print("Enter the names of vertices (separate names by space):")
    vertices = input().split()
    count = 0  # Initialize count here
    return graph, vertices

def NextValue(k):
    while True:
        x[k] = (x[k] + 1) % (colors + 1)
        if x[k] == 0:
            return
        for j in range(n):
            if graph[k][j] == 1 and x[k] == x[j]:
                break
        if j == n - 1: """be careful with this"""
            return

def GraphColoring(k):
    global count  # Define count as global
    while True:
        NextValue(k)
        if x[k] == 0:
            return   # no new color possible
        if k == n - 1:  # All vertices have been colored
            count += 1  
            print(x)
        else:
            GraphColoring(k + 1)

# Example usage:
graph, vertices = input_graph()
colors = int(input("Enter the number of colors: "))
x = [0] * n

GraphColoring(0)
print("Total colorings:", count)
