# Write your solution here
def length_of_longest(my_list):
    longest_word = ""
    longest_length = 0

    for word in my_list:
        actual_length = len(word)
        if actual_length > longest_length:
            longest_length = actual_length
            longest_word = word

    return longest_length

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = length_of_longest(my_list)
    print(result)