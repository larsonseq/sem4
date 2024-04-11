print("Larson Sequeira  Roll No 36    PID: 222104")
#input the number
n = input("Enter a Number: ")

power = 0

for i in n:
    power += pow(int(i), len(n))

if power == int(n):
    print("The number is an armstrong number")

else:
    print("The number is not an armstrong number")