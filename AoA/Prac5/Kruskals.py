MAX = 30

class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

class EdgeList:
    def __init__(self):
        self.data = [Edge(0, 0, 0) for _ in range(MAX)]
        self.n = 0

elist = EdgeList()
G = [[0] * MAX for _ in range(MAX)]
n = 0
spanlist = EdgeList()

def kruskal():
    global elist, G, n, spanlist
    belongs = [i for i in range(n)]
    elist.n = 0

    for i in range(1, n):
        for j in range(i):
            if G[i][j] != 0:
                elist.data[elist.n] = Edge(i, j, G[i][j])
                elist.n += 1

    sort()
    for i in range(n):
        belongs[i] = i

    spanlist.n = 0
    for i in range(elist.n):
        cno1 = find(belongs, elist.data[i].u)
        cno2 = find(belongs, elist.data[i].v)
        if cno1 != cno2:
            spanlist.data[spanlist.n] = elist.data[i]
            spanlist.n += 1
            union1(belongs, cno1, cno2)

def find(belongs, vertexno):
    return belongs[vertexno]

def union1(belongs, c1, c2):
    for i in range(n):
        if belongs[i] == c2:
            belongs[i] = c1

def sort():
    global elist
    for i in range(1, elist.n):
        for j in range(elist.n - 1):
            if elist.data[j].w > elist.data[j + 1].w:
                elist.data[j], elist.data[j + 1] = elist.data[j + 1], elist.data[j]

def print_result():
    global spanlist, n
    cost = 0
    for i in range(spanlist.n):
        print("\nu v w")
        print(f"{spanlist.data[i].u} {spanlist.data[i].v} {spanlist.data[i].w}")
        cost += spanlist.data[i].w

    print(f"\n\ncost of the spanning tree: {cost}")

def main():
    global G, n
    total_cost = 0
    print("\nenter number of vertices: ")
    n = int(input())
    print("\nenter the adjacency matrix:")
    for i in range(n):
        G[i] = list(map(int, input().split()))

    kruskal()
    print_result()

if __name__ == "__main__":
    main()