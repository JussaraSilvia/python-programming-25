# Write your solution here
limit = int(input("Limit: "))
sum_total = 0
number = 1

while sum_total < limit:
    sum_total += number
    number += 1

print(sum_total)