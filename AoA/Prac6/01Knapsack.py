MAX = 100

def main():
    n = int(input("Enter the number of elements: "))
    flag = [0] * MAX
    v = [0] * MAX
    w = [0] * MAX
    m = [[0] * (MAX + 1) for _ in range(MAX + 1)]
    
    print("Enter the weights: ", end="")
    for i in range(1, n + 1):
        w[i] = int(input())

    print("Enter the values: ", end="")
    for i in range(1, n + 1):
        v[i] = int(input())
        
    W = int(input("Enter the capacity of knapsack: "))
    
    print("Matrix is as follows: ")
    for j in range(W + 1):
        m[0][j] = 0
    
    for i in range(1, n + 1):
        for j in range(W + 1):
            if w[i] <= j:
                m[i][j] = max(m[i - 1][j], m[i - 1][j - w[i]] + v[i])
            else:
                m[i][j] = m[i - 1][j]
    
    i = n
    k = W
    while i > 0 and k > 0:
        if m[i][k] != m[i - 1][k]:
            flag[i] = 1
            k = k - w[i]
            i = i - 1
        else:
            i -= 1
    
    print("\t", end="")
    for i in range(W + 1):
        print(f"{i}\t", end="")
    print("")
    
    for i in range(10 * W + 1):
        print("-", end="")
    print("")
    
    for i in range(n + 1):
        print(f"{i}  |\t", end="")
        for j in range(W + 1):
            print(f"{m[i][j]}\t", end="")
        print("")
    
    print("The resultant vector is ", end="")
    print("( ", end="")
    for i in range(1, n + 1):
        print(f"{flag[i]}, ", end="")
    print(")")
    
    print(f"The total profit is: {m[n][W]}")
    print("The objects selected are: ")
    print("Weight \tProfit")
    for i in range(1, n + 1):
        if flag[i] == 1:
            print(f"{w[i]}\t{v[i]}")

if __name__ == "__main__":
    main()