# Copy here code of line function from previous exercise and use it in your solution
def line(number, string):
    if string == "":
        print("*" * number)
    else:
        print(string[0] * number)

def shape(height, char1, width, char2):
    for i in range(1, height + 1):
        line(i, char1)
    for j in range(width):
        line(i, char2)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")