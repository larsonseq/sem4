
def quick_sort(arr, start, end): 
    if start < end:
        new_pivot = partition(arr, start, end)
        quick_sort(arr, start, new_pivot - 1)
        quick_sort(arr, new_pivot + 1, end)


def partition(arr, start, end): 
    pivot = arr[start]
    print(f"Pivot was {pivot}\t", end="")
    i = start + 1

    for j in range(start + 1, end + 1):
        if arr[j] < pivot:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1

    temp = arr[start]
    arr[start] = arr[i - 1]
    arr[i - 1] = temp
    print(f"array is {arr}")

    return (i - 1)


if __name__ == "__main__":
    print("Larson Sequeira \t Roll No: 36 \t PID: 222104")
    n = int(input("Enter number of elements: "))
    arr = []

    for i in range(0, n):
        x = int(input(f"Enter element {i + 1}: "))
        arr.append(x)

    print(f"before sorting, array is : {arr}")
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)
