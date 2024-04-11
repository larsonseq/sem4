#Larson Sequeira  Roll No 36  SE CMPN B
list1 = ["apple", "grapes", "oranges"]
try:
    print(f"Trying to access index 5 of {list1}")
    print(list1[5])
except Exception as e:
    print("Exception Occured")
    print(f"Exception was :{e}")
finally:
    print("Finally was Executed\n")

#getting partiular exception
num1 = 100
num2 = 0
try:
    print(f"dividing {num1} by {num2}")
    num3 = num1 / num2
except ZeroDivisionError:
    print("Exception Occured\nCannot divide by 0")