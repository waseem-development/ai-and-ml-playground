print("hello")
default_num = 3
while True:
    num = int(input("Enter a number to divide 3 by it: "))
    print(default_num/num)
# print("Hello World")
# def average(a,b):
#     return (a + b) / 3 # LogicalError
# print(average(12, 60))
# print("Bye World" SyntaxError

# while True:
#     age = int(input("Enter a number: "))

# def average(a, b):
#     # return a + b / 2 # LogicalError
#     return (a + b) / 2 # Fixed Code
# print(average(12, 60))

# a = [22121,2,22,1,2,12]
# print(a[6])

a = {
    "ab": 3123,
    "cd": 4141,
}
# print(a["de"])
# raise ZeroDivisionError("COme on DUde u cannot divide anything by 0")


# ***************** TypeError Examples *****************


# 1. String + Integer
# age = 20
# print("Age: " + age)


# 2. Integer + List
x = 10
numbers = [1, 2, 3]
# print(x + numbers)


# 3. Calling a String like a Function
name = "Paxto"
# name()


# ***************** ValueError Examples *****************
int("abc")

# 1. Invalid Integer Conversion
# number = int("hello")


# 2. Removing a Value that Doesn't Exist
numbers = [1, 2, 3]
# numbers.remove(10)


# 3. Square Root of a Negative Number
# import math
# print(math.sqrt(-1))