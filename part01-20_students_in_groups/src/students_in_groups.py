# Write your solution here
students = int(input("How many students on the course? "))
size = int(input("Desired group size? "))

groups = int(students // size)
resto = int(students % size)


if resto >= 1:
    groups += 1

print("Number of groups formed:", groups)