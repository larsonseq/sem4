import numpy as np
 
# Demonstrate linspace
points = np.linspace(0, 10, 5)
print("Generated points using linspace:", points)

# Demonstrate arange
values = np.arange(0, 10, 2)
print("Generated values using arange:", values)

# Demonstrate aggregate functions
arr = np.array([1, 2, 3, 4, 5])

# Sum of array
print("Sum of array:", np.sum(arr))

# Max value of array
print("Max value of array:", np.max(arr))

# Mean of array elements
print("Mean of array elements:", np.mean(arr))
 