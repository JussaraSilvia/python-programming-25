# Write your solution here
def all_the_longest(my_list: list):
    longest_length = 0
    result = []

    for word in my_list:
        length = len(word)
        if length > longest_length:
            longest_length = length
            result = [word]        
        elif length == longest_length:
            result.append(word)  
    return result

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    print(all_the_longest(my_list))  # ['eleventh']