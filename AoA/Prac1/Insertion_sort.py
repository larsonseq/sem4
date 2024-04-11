print("Larson Sequeira    Roll No: 36    PID: 222104")
n = int(input("Enter size of list: "))
array = []
for i in range(0, n):
    x = int(input(f"Enter element {i+1}: "))
    array.append(x)

print(f"List Before Sorting: {array}")

for j in range(1, n):
    key = array[j]
    i = j - 1
    while i >= 0 and array[i] > key:
        array[i+1] = array[i]
        i = i - 1
    array[i+1] = key
    
print(f"List after sorting: {array}")