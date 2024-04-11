with open(r"myfile.txt", 'r') as f:
    print("myfile.txt contains:")
    data= f.readlines()
    print(data)
    for i in data:
        print(i,end="")
    print("\n")
 
with open(r"myfile.txt",'a') as f:
    data = input("Enter a line to append:").strip() + "\n"
    f.write(data)
    print("Done writing data\n")
 
with open(r"myfile.txt", 'r') as f:
    data= f.readlines()
    print("myfile.txt contains:")
    print(data)
    for i in data:
        print(i, end="")
    print("\n")