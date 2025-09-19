# Write your solution here
def list_of_stars(stars):
    for i in stars:
        print("*" * i)

if __name__ == "__main__":
    stars = [3, 7, 1, 1, 2]
    list_of_stars(stars)