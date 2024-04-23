import sys

def ExtractMin(d, sptset, size):
    min_val = sys.maxsize
    min_index = 0
    for i in range(size):
        if not sptset[i] and d[i] < min_val:
            min_val = d[i]
            min_index = i
    return min_index

def printPath(paths, src, dest):
    path = []
    node = dest
    while node != src:
        path.append(chr(ord('A') + node))
        node = paths[node]
    path.append(chr(ord('A') + src))
    print('->'.join(reversed(path)), end=' ')

if __name__ == "__main__":
    size = int(input("Enter number of nodes: "))
    cost = []
    print("Enter The cost matrix:")
    for i in range(size):
        temp = list(map(int, input().split()))
        cost.append(temp)
    print(cost)
    
    src = int(input("Enter source: "))
    pie = [-1] * size
    d = [sys.maxsize] * size
    sptset = [False] * size
    d[src] = 0

    for _ in range(size):
        u = ExtractMin(d, sptset, size)
        sptset[u] = True

        for v in range(size):
            if cost[u][v] > 0 and not sptset[v]:
                if d[v] > (d[u] + cost[u][v]):
                    d[v] = d[u] + cost[u][v]
                    pie[v] = u
    
    print("Vertex\tDistance\tShortest Path")
    for i in range(size):
        print(f"{chr(ord('A') + i)}\t{d[i]}\t\t", end='')
        printPath(pie, src, i)
        print()
