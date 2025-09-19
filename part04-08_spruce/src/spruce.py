# Write your solution here
def spruce(number):
    print("a spruce!")
    for i in range(1, number + 1):
        left = number - i
        asterisks = 2 * i - 1
        print(left * " " + asterisks * "*")

    print((number - 1) * " " + "*")
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)