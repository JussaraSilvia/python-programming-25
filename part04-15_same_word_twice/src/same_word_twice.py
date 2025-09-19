# Write your solution here
sequence = []

while True:
    word = input("Word: ")
    sequence.append(word)

    if len(sequence) != len(set(sequence)):
        print(f"You typed in {len(sequence) - 1} different words")
        break