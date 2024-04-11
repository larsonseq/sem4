def sum_of_subsets(s, k, r, w, x, m):
    x[k] = 1
    if s + w[k] == m:
        print_solution(x, w)
    elif s + w[k] + w[k + 1] <= m:
        sum_of_subsets(s + w[k], k + 1, r - w[k], w, x, m)
    if s + r - w[k] >= m and s + w[k + 1] <= m:
        x[k] = 0
        sum_of_subsets(s, k + 1, r - w[k], w, x, m)


def print_solution(x, w):
    subset = []
    for i in range(len(x)):
        if x[i] == 1:
            subset.append(w[i])
    print(f"the solution is {tuple(subset)}")
    print(" and the vector is [", end=" ")
    for x in w:
        if x in subset:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print("]")
   

def generate_subsets(w, S):
    n = len(w)
    x = [0] * n
    r = sum(w)
    sum_of_subsets(0, 0, r, w, x, S)

# Example usage:
n = int(input("Enter the number of elements: "))
w = []
for i in range(n):
    w.append(int(input("Enter element {}: ".format(i + 1))))
S = int(input("Enter the target sum: "))
w.sort()
generate_subsets(w, S)