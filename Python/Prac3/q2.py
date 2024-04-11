with open(r"myfile.txt", 'r') as f:
    data= f.readlines()
    print("myfile.txt contains:") 
    for i in data:
        print(i, end="")
    print("\n")
    f.close()
    
with open(r"myfile.txt", 'r') as f:
    data = f.readlines()

print('Total Number of lines:', str(len(data)))