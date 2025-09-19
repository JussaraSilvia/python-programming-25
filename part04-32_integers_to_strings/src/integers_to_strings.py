# Write your solution here
def formatted(my_list):
    result = []
    for number in my_list:
        new_string = f"{number:.2f}"
        result.append(new_string)
    return result

if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)