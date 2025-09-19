# Write your solution here
def even_numbers(my_list):
    even = [i for i in my_list if i % 2 == 0]
    return even

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)