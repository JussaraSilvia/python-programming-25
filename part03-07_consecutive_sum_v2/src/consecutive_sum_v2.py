# Write your solution here
limit = int(input("Limit: "))
sum_total = 0
number = 1
equation = ""

while sum_total < limit:
    sum_total += number
    if number == 1:
        equation = equation + str(number)
    else:
        equation = equation + " + " + str(number)
    number += 1

print(f"The consecutive sum: {equation} = {sum_total}")