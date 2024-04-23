
def sumOfSubsets(s, k, r, w, m, x):
    x[k] = 1 
    if (s + w[k]) == m :
        print(x) 
    elif (s + w[k] + w[k+1]) <= m:
        sumOfSubsets(s+w[k], k+1, r-w[k], w, m, x)
    if ((s + (r - w[k]))>=m) and (s + w[k+1])<=m:
        x[k] = 0
        sumOfSubsets(s, k+1, r-w[k], w, m, x)


def generate_subsets(x, m, n):
    x = [0] * len(x)
    s = 0
    k = 0
    r = 0
    for i in w:
        r = r + i
    
    sumOfSubsets(s, k, r, w, m, x)


if __name__ == "__main__":
    n = int(input("Enter Number of ELements"))
    w = []
    for i in range(n):
        w.append(int(input(f"Enter {i+1} element:")))
    
    m = int(input(f"Enter Target sum: "))
    generate_subsets(w, m, n)