def MergeSort(A, low, high):
    if low < high:
        mid = int((high + low)/2)
        MergeSort(A, low, mid)
        MergeSort(A, mid+1, high)
        Merge(A, low, mid, high)

def Merge(A, low, mid, high):
    h = low
    i = low
    j = mid+1
    B = [0] * (high+1)
    while h <= mid and j <= high:
        if A[h] <= A[j]:
            B[i] = A[h]
            h += 1
        else:
            B[i] = A[j]
            j += 1
        i += 1
    
    while j <= high:
        B[i] = A[j]
        j += 1
        i += 1
    while h <= mid:
        B[i] = A[h]
        h += 1
        i += 1
    
    for k in range(low, high+1):
        A[k] = B[k]
    print(f"A is {A}\t\t B is {B}")

A = [4,6,44,2,3,8,4,2,8,2]
MergeSort(A, 0, len(A)-1)
print(A)