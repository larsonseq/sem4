def trace(V, w, p, n, m):
    sp = 0
    sw = 0
    i = n
    j = m
    x = [0] * i 
    while j > 0:
        if V[i][j] == V[i-1][j]:
            i = i -1
        else:
            x[i-1] = 1
            sw = sw + w[i-1]
            sp = sp + p[i-1]
            j = j - w[i-1]
            i = i-1
    print(f"{x}\n{sp, sw}\n")

if __name__ == "__main__":
    capacity = int(input("Enter size of array: "))
    w = list(map(int, input("Enter weights: ").split()))
    p = list(map(int, input("Enter profits: ").split()))

    V = [[0] * (capacity+1) for i in range(len(w)+1)]

    for i in range(len(w)):
        V[i][0] = 0
    for j in range(capacity):
        V[0][j] = 0
    
    for i in range(1,len(w)+1):
        for j in range(1, capacity+1):
            if w[i-1] <= j: 
                V[i][j] = max(V[i-1][j], p[i-1] + V[i-1][j-w[i-1]])
            else:
                V[i][j] = V[i-1][j]
    
    for i in range(len(V)):
        print(V[i])
    
    trace(V, w, p, len(w), capacity)