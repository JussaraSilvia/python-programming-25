# Write your solution here
def sum_of_positives(my_list):
    positives = [i for i in my_list if i > 0]
    return sum(positives)

if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)