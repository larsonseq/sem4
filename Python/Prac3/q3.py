import os
 
print(f"Current working directory: {os.getcwd()}")
files = os.listdir()
for i in files:
    print(i)