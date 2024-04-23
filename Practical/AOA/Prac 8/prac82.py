# Sum of Subsets

def sum_of_subsets(s, k, r, w, x, m):
    x[k] = 1
    if (s + w[k]) == m:
        print(x)
    elif ((s + w[k] + w[k+1]) <= m):
        sum_of_subsets(s+w[k], k+1, r-w[k], w, x.copy(), m)
    if ((s + (r - w[k])) >= m) and ((s + w[k+1]) <= m):
        x[k] = 0
        sum_of_subsets(s, k+1, r-w[k], w, x.copy(), m)
    
    """
    when calling sum_of_subsets function recursively,
    pass a copy of the list x, ie pass by value
    because if passed by reference, it will cause error in the subset vector of the solution
    it will include the past answer found in the statespace tree in the next state of the state space tree
    forget above sentence, idk what i typed
    try m = 7, n = 5, w = [1, 2, 3, 4, 5]
    try by using x.copy() and without using x.copy in the sub_of_subsets() recursive call
    """


def generate(n, m, w):
    x = [0] * n 
    r = 0
    for i in w:
        r = r + i
    s = 0
    k = 0
    sum_of_subsets(s, k, r, w, x, m)

if __name__ == "__main__":
    n = int(input("Enter number of Elements in the Subset: "))

    m = int(input(f"Enter Target Sum: "))

    w = []
    for i in range(n):
        temp = int(input(f"Enter {i+1} element of the subset: "))
        w.append(temp)

    generate(n, m, w) 