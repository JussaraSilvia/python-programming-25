# Write your solution here
hourly = float(input("Hourly wage: "))
hours = int(input("Hours worked: "))
day = input("Day of the week: ")

if day != "Sunday":
    daily = hourly * hours

if day == "Sunday":
    hourly *=2
    daily = hourly * hours

print("Daily wages:", daily,"euros")