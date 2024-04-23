def QuickSort(A, lb, ub):
    if ub > lb:
        pivot = Partition(A, lb, ub)
        QuickSort(A, lb, pivot-1)
        QuickSort(A, pivot+1, ub)

def Partition(A, lb, ub):
    up = ub
    down = lb
    x = A[lb]
    print(f"{down}, {up}, {A}")
    while down < up:
        while A[down] <= x and down < up:
            down = down + 1
        while A[up] > x:
            up = up - 1
        if down <= up :
            temp = A[up]
            A[up] = A[down]
            A[down] = temp
    
    A[lb] = A[up]
    A[up] = x
    return up

A = [9,8,7,6,5,4,3,2,1,0]
QuickSort(A, 0, len(A)-1)
print(A)