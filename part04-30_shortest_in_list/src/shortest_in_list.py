# Write your solution here
def shortest(my_list):
    short_word = my_list[0]
    short_length = len(my_list[0])

    for word in my_list:
        actual_length = len(word)

        if actual_length < short_length:
            short_length = actual_length
            short_word = word

    return short_word

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = shortest(my_list)
    print(result)
