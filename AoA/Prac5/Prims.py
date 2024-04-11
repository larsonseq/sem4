infinity = 9999
MAX = 20

G = [[0] * MAX for _ in range(MAX)]
spanning = [[0] * MAX for _ in range(MAX)]
n = 0

def prims():
    global G, spanning, n
    cost = [[0] * MAX for _ in range(MAX)]
    u, v, min_distance, distance, from_vertex = 0, 0, 0, [0] * MAX, [0] * MAX
    visited = [0] * MAX
    no_of_edges, i, min_cost, j = 0, 0, 0, 0

    for i in range(n):
        for j in range(n):
            if G[i][j] == 0:
                cost[i][j] = infinity
            else:
                cost[i][j] = G[i][j]
            spanning[i][j] = 0

    distance[0] = 0
    visited[0] = 1

    for i in range(1, n):
        distance[i] = cost[0][i]
        from_vertex[i] = 0
        visited[i] = 0

    min_cost = 0
    no_of_edges = n - 1

    while no_of_edges > 0:
        min_distance = infinity
        for i in range(1, n):
            if visited[i] == 0 and distance[i] < min_distance:
                v = i
                min_distance = distance[i]

        u = from_vertex[v]
        spanning[u][v] = distance[v]
        spanning[v][u] = distance[v]
        no_of_edges -= 1
        visited[v] = 1

        for i in range(1, n):
            if visited[i] == 0 and cost[i][v] < distance[i]:
                distance[i] = cost[i][v]
                from_vertex[i] = v

        min_cost += cost[u][v]

    return min_cost

def main():
    global G, n
    total_cost = 0
    print("enter no. of vertices: ")
    n = int(input())
    print("\nenter the adjacency matrix: \n")
    for i in range(n):
        G[i] = list(map(int, input().split()))

    total_cost = prims()
    print("\nspanning tree matrix: ")
    for i in range(n):
        print("\n")
        for j in range(n):
            print(spanning[i][j], end=" ")

    print("\n\ntotal cost of spanning tree is:", total_cost)

if __name__ == "__main__":
    main()
