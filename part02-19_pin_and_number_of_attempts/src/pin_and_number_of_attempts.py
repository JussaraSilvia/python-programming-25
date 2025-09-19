# Write your solution here
attempts = 0

while True:
    attempts += 1
    pin = input("PIN: ")

    if pin != "4321":
        print("Wrong")
    elif pin == "4321" and attempts > 1:
        print("Correct! It took you", attempts, "attempts")
        break
    else:
        print("Correct! It only took you one single attempt!")
        break