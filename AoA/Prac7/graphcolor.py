def is_safe(graph, v, color, c):
    for i in range(len(graph)):
        if graph[v][i] and color[i] == c:
            return False
    return True

def graph_coloring_util(graph, m, color, v, vertices):
    if v == len(graph):
        print(vertices)
        print_solution(color, vertices)
        return True

    res = False
    for c in range(1, m + 1):
        if is_safe(graph, v, color, c):
            color[v] = c
            res = graph_coloring_util(graph, m, color, v + 1, vertices) or res
            color[v] = 0
    return res

def print_solution(color, vertices):
    print(color)
    print()

def graph_coloring(graph, m, vertices):
    color = [0] * len(graph)
    if not graph_coloring_util(graph, m, color, 0, vertices):
        print("No solution exists.")

# Function to take user input for graph
def input_graph():
    n = int(input("Enter the number of vertices in the graph: "))
    graph = [[0] * n for _ in range(n)]
    vertices = [None] * n
    print("Enter the adjacency matrix of the graph (separate elements by space):")
    for i in range(n):
        graph[i] = list(map(int, input().split()))
    print("Enter the names of vertices (separate names by space):")
    vertices = input().split()
    return graph, vertices

# Example usage:
graph, vertices = input_graph()
colors = int(input("Enter the number of colors: "))
graph_coloring(graph, colors, vertices)