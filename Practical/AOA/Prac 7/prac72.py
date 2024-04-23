
def GraphColoring(k):
    global count
    global x
    while True:
        NextValue(k)
        if x[k] == 0:
            return
        if k == n - 1:
            print(x)
            count += 1
        else:
            GraphColoring(k+1)

def NextValue(k):
    while True:
        x[k] = (x[k] + 1) % (colors + 1)
        if x[k] == 0:
            return
        for j in range(n):
            if G[k][j] == 1 and x[k] == x[j]:
                break
        if j == n-1:
            return

if __name__ == "__main__":
    global x
    global count
    n = int(input(f"Enter number of nodes: "))
    print(f"Enter Adjacency matrix: ")
    G = []
    for i in range(n):
        temp1 = list(map(int, input().split()))
        G.append(temp1)
    
    colors = int(input(f"Enter Number of Colors: "))
    count = 0
    x = [0] * n
    GraphColoring(0)
    print(f"Number of colors is {count}")
