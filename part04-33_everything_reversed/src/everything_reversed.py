# Write your solution here
def everything_reversed(my_list: list):
    reversed_list = []

    for word in reversed(my_list):
        reversed_word = word[::-1]   
        reversed_list.append(reversed_word)

    return reversed_list

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)