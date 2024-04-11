print("Larson Sequeira  Roll No 36    PID: 222104")

# Create a set
fruits = {"apple", "banana", "cherry"}
print(f"The set contains: {fruits}")

# Get the length of a set
print(f"The length of the set is: {len(fruits)}")

# Get the type of data structure
print(f"The type of data structure is {type(fruits)}")

# Set constructor
thisset = set(("apple", "mango", "grapes", "oranges"))
print(f"Used constructor to create this set which contains: {thisset}")

# Loop through set items
print("Printing the set using a for loop")
for x in thisset:
    print(x)

# Check if an element is in a set
print("Is 'mango' in this set?", "mango" in thisset)

# Add elements to the set
thisset.add("cherry")

# Add elements from another set
temp = ("papaya", "kiwi")
thisset.update(temp)

# Remove items
try:
    thisset.remove("chikkoo")
except KeyError as e:
    print(f"Error: {e}. 'chikkoo' not found in the set.")
print(f"After removal attempt: {thisset}")

# Discard an element
thisset.discard("guava")
print(f"After discarding 'guava': {thisset}")

# Delete a random element using 'pop'
thisset.pop()
print(f"After popping a random element: {thisset}")

# Clear a set
thisset.clear()
print(f"The set was cleared. It now contains: {thisset}")

# Delete a set
del thisset

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}

# Union of two sets
set3 = set1.union(set2)
print(f"Union of set1 and set2: {set3}")

# Join two sets using update
set1.update(set2)
print(f"Joined set1 and set2 using update: {set1}")

# Intersection of two sets
set1 = {"apple", "banana", "cherry"}  # Re-creating set1
set3 = set1.intersection(set2)
print(f"Intersection of set1 and set2: {set3}")

# Symmetric difference
set3 = set1.symmetric_difference(set2)
print(f"Symmetric difference of set1 and set2: {set3}")

# Check if a set is a subset or not
print(f"Is set1 a subset of set2? {set1.issubset(set2)}")
