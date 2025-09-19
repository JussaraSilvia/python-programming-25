# Write your solution here
numbers = []
i = 1

while True:
    print(f"The list is now {numbers}")
    item = input("a(d)d, (r)emove or e(x)it: ")
    if item == "x":
        print("Bye!")
        break
    if item == "d":
        numbers.append(i)
        i += 1
    if item == "r":
        numbers.pop()
        i -= 1