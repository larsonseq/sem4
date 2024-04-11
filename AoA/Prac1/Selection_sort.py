print("Larson Sequeira    Roll No: 36    PID: 222104")
n = int(input("Enter size of list: "))
array = []
for i in range(0, n):
    x = int(input(f"Enter element {i+1}: "))
    array.append(x)

print(f"List Before Sorting: {array}")

for i in range(0, n):
    j = i
    for k in range((i+1), n):
        if array[k] < array[j]:
            j = k
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

print(f"List after sorting: {array}")