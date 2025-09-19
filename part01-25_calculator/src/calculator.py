# Write your solution here
x = int(input("Number 1: "))
y = int(input("Number 2: "))
operation = input("Operation: ")

if operation == "add":
    z = x + y
    print(x,"+",y,"=", z)

if operation == "multiply":
    z = x * y
    print(x,"*", y,"=", z)

if operation == "subtract":
    z = x - y
    print(x, "-", y, "=", z)