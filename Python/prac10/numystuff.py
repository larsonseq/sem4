import numpy as np

#shape
print("Shape:")
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)

#reshape
print("Reshape:") 
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(f"Reshape {arr} to (3,4)")
newarr = arr.reshape(4, 3)
print(newarr)
 
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(f"Reshape {arr} to (2,3,2)")
newarr = arr.reshape(2, 3, 2)
print(newarr)
print("")

#sorting array
arr = np.array([3, 2, 0, 1])
print(f"Sorting Array: {arr}")
print(np.sort(arr))

# Generating 5 points between 0 and 10
points = np. linspace(0, 10, 5)
print("Generated Points:", points)

# Generating values from 0 to 9 with a step of 2
values = np.arange(0, 10, 2)
print("Generated Values:", values)
 
#slicing
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(f"SLiced array: {arr[1:5]}")
print(arr[4:])

#copy
print("Numpy Copy")
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)

#dimension
#0 d
print("0 Dimension")
arr = np.array(42)
print(arr)
#1d
print("1 Dimension")
arr = np.array([1, 2, 3])
print(arr)
#2d
print("2 Dimension")
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
#3d
print("3 Dimension: ")
arr = np.array([ [[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]] ])
print(arr)

#view
print("View:")
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42
print(arr)
print(x)
