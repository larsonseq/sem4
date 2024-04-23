import sys

def ExtractMin(d, spt, size):
    min_val = sys.maxsize
    min_index = 0
    for i in range(size):
        if not spt[i] and d[i] < min_val:
            min_val = d[i]
            min_index = i
    return min_index

def pathFinder(paths, src, dest):
    p = []
    node = dest
    while node != src:
        p.append(chr(ord('A') + node))
        node = paths[node]
    p.append(chr(ord('A')+src))
    print("->".join(reversed(p)), end = "")

if __name__ == "__main__":
    size = int(input(f"Enter number of nodes: "))

    cost = []

    print("Enter Cost Matrix: ")
    for i in range(size):
        temp = list(map(int, input().split()))
        cost.append(temp)
    
    pie = [-1] * size
    distance = [sys.maxsize] * size
    sptset = [False] * size

    src = int(input("Enter the starting vertex(0-indexed): "))
    distance[src] = 0
    pie[src] = src

    for j in range(size):
        u = ExtractMin(distance, sptset, size)
        sptset[u] = True

        for v in range(size):
            if cost[u][v] > 0 and not sptset[v]:
                if distance[v] > distance[u] + cost[u][v]:
                    distance[v] = distance[u] + cost[u][v]
                    pie[v] = u

    print(f"Vertex\t\tdistance")
    for i in range(size):
        print(f"{chr(ord('A') + i)}\t   {distance[i]}")

    for i in range(size):
        pathFinder(pie, src, i)
        print("")