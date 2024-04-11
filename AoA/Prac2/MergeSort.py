def merge_sort(A, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(A, low, mid)
        merge_sort(A, mid + 1, high)
        merge(A, low, mid, high) 
  
    return A


def merge(A, low, mid, high):
    i = low
    j = mid + 1
    k = low
    B = [0] * (high + 1)

    while i <= mid and j <= high:
        if A[i] <= A[j]:
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1
        k += 1

    while i <= mid:
        B[k] = A[i]
        i += 1
        k += 1

    while j <= high:
        B[k] = A[j]
        j += 1
        k += 1

    for k in range(low, high + 1):
        A[k] = B[k]
    
    print(f"After Merge: {A}\n")


if __name__ == "__main__":
    print("Larson Sequeira \t Roll No: 36 \t PID: 222104")
    n = int(input("Enter Number of elements: "))
    array = []
    for i in range(0, n):
        temp = int(input(f"Enter element {i+1}:"))
        array.append(temp)

    print(f"Unsorted array: {array}")
    array = merge_sort(array, 0, (n-1))
    print(f"Sorted array: {array}")