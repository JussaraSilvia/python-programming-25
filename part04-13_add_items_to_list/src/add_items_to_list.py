# Write your solution here
items = []
many_items = int(input("How many items: "))

for i in range(many_items):
    item = int(input(f"Item {i}: "))
    items.append(item)
print(items)