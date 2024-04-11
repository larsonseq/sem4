print("Larson Sequeira  Roll No 36    PID: 222104")

# Create a list
mylist = ["apple", "banana", "cherry"]
print(f"The list is: {mylist}")

# Print the length of the list
print(f"The length of mylist is {len(mylist)}")

# Create a list using list constructor
thislist = list(("apple", "banana", "orange", "kiwi", "melon", "mango"))
print(f"This list is created using a list constructor: {thislist}")

# Access items in thislist
print(f"The element at the 2nd position is {thislist[1]}")

# Print the last element in the list
print(f"The last element in the list is {thislist[-1]}")

# Print a range of indexes
print(f"Elements from 1 to 3 of this list are: {thislist[0:2]}")
print(f"Elements from 3rd position to the end are: {thislist[2:]}")
print(f"Elements from the last to the 5th position are: {thislist[-1:-5:-1]}")
print(f"Elements at even indexes are: {thislist[::2]}")

# Check if an item is in the list
if "apple" in thislist:
    print("Yes, apple is in the list.")
else:
    print("No, apple isn't there in the list.")

# Sort the list
thislist.sort()
print(f"The list sorted in ascending order: {thislist}")

# Sort the list in reverse
thislist.sort(reverse=True)
print(f"The list sorted in descending order: {thislist}")
thislist.reverse()

# Insert items
thislist.append("watermelon")
print(f"Watermelon added to the end: {thislist}")

# Insert at a location
thislist.insert(2, "grapes")
print(f"Grapes inserted at position 2: {thislist}")

# Add an item to the end of the list
thislist.append("guava")
print(f"Guava added to the end: {thislist}")

# Add items from another list or data structure
thatlist = ["cherry", "pineapple"]
thislist.extend(thatlist)
print(f"Elements from 'thatlist' added to 'thislist': {thislist}")

# Remove an item
thislist.remove("pineapple")
print(f"Pineapple removed: {thislist}")

# Remove an item at an index
thislist.pop(2)
print(f"Element at position 2 removed: {thislist}")

# Remove the last item
thislist.pop()
print(f"Last element removed: {thislist}")

# Delete an item using 'del'
del thislist[4]
print(f"Element at position 4 deleted: {thislist}")

# Clear the list
thislist.clear()
print(f"The list was cleared. It now contains: {thislist}")

# Delete the list
del thislist
print(f"The list was deleted. Accessing it results in: {thislist}")
