print("Larson Sequeira  Roll No 36    PID: 222104")

# Create a dictionary
thisdict = {
  "lname" : "doe",
  "fname" : "john",
  "age" : 20,
}

# Print the dictionary
print(f"The dictionary is: {thisdict}")

# Get the value of a key
print(f"The value of the 'age' key is: {thisdict['age']}")

# Get the length of the dictionary
print(f"The length of the dictionary is: {len(thisdict)}")

# Get the value of the "age" key using get method
age = thisdict.get("age")
print(f"The value of the 'age' key using get method is: {age}")

# Get a list of the keys
print(f"The list of keys in the dictionary: {list(thisdict.keys())}")

# Get a list of the values
print(f"The list of values in the dictionary: {list(thisdict.values())}")

# Change the value of a key
print("Changing the value of the 'age' key")
thisdict["age"] = 21
print(f"The updated value of the 'age' key is: {thisdict['age']}")

# Loop through the dictionary
print("Printing Key:value pairs:")
for key in thisdict.keys():
    print(f"{key}: {thisdict[key]}")

for value in thisdict.values():
    print(value)

for key, value in thisdict.items():
    print(key, value)

print("\n")

# Add key-value pair to the dictionary
thisdict["rollno"] = 36
thisdict["gender"] = "male"
print(f"The dictionary after adding new key-value pairs: {thisdict}")

# Get the type of the dictionary
print(f"The type of the dictionary is: {type(thisdict)}")

# Remove an item
thisdict.pop("gender")
print(f"The dictionary after removing 'gender': {thisdict}")

# Delete a key
del thisdict["age"]
print(f"The dictionary after deleting the 'age' key: {thisdict}")

# Clear the dictionary
thisdict.clear()
print(f"The dictionary was cleared. It now contains: {thisdict}")

# Delete the dictionary
del thisdict
print(f"The dictionary was deleted. Accessing it results in: {thisdict}")
