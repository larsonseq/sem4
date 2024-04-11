print("Larson Sequeira  Roll No 36    PID: 222104")

# Define a tuple
fruits = ("apple", "mango", "grapes", "oranges", "guava", "chikkoo", "banana")
print(f"The tuple is: {fruits}")

# Loop through the tuple
for i in fruits:
    print(i)

# Get the type of the tuple
print(f"The type of 'fruits' is: {type(fruits)}")

# Get the length of the tuple
print(f"The length of 'fruits' is: {len(fruits)}")

# Create a tuple using a tuple constructor
numbers = tuple((1, 2, 3, 4, 5, 6, 7, 8))
print(f"The tuple 'numbers' is: {numbers}")

# Add items to tuples
temp = list(fruits)
temp.append("pineapple")
fruits = tuple(temp)
print(f"Pineapple added to 'fruits': {fruits}")

# Deleting items from tuples
temp = list(fruits)
temp.remove("pineapple")
fruits = tuple(temp)
print(f"Pineapple removed from 'fruits': {fruits}")

# Unpacking tuples
a, b, c, *d = fruits
print(f"Unpacked values: {a}, {b}, {c}, {d}")

# Join two tuples
fruits_and_numbers = fruits + numbers
print(f"Joined tuple 'fruits' and 'numbers': {fruits_and_numbers}")

# Count number of repetitions of an element in a tuple
print(f"Number of occurrences of 'mango' in 'fruits': {fruits.count('mango')}")

# Deleting an element from tuple is not allowed, so this line will result in an error:
# del fruits[0]
# Instead, you can convert it to a list, delete the element, and convert it back to a tuple.

# Delete the tuple
del fruits
print("The tuple 'fruits' was deleted. Accessing it results in an error.")
