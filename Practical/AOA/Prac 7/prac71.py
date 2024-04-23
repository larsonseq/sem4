count = 0

def is_safe(graph, v, color, c):
    """
    Check if it's safe to assign color c to vertex v.
    """
    for i in range(len(graph)):
        if graph[v][i] and color[i] == c:
            return False
    return True

def graph_coloring_util(graph, m, color, v, vertices):
    """
    Backtracking utility function to find all possible graph colorings.
    """
    if v == len(graph):
        print(vertices)
        print_solution(color)
        return True

    res = False
    for c in range(1, m + 1):
        if is_safe(graph, v, color, c):
            color[v] = c
            res = graph_coloring_util(graph, m, color, v + 1, vertices) or res
            color[v] = 0
    return res

def print_solution(color):
    """
    Print the solution color assignment.
    """
    print("Coloring:", color)
    global count
    count += 1
    print()

def graph_coloring(graph, m, vertices):
    """
    Main function to perform graph coloring.
    """
    color = [0] * len(graph)
    if not graph_coloring_util(graph, m, color, 0, vertices):
        print("No solution exists.")







def input_graph():
    """
    Function to take user input for graph.
    """
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
print(count)