# List of words to search
words = [
    "apple", "banana", "apricot", "blueberry", "avocado",
    "cherry", "date", "elderberry", "fig", "grape", "guava"
]

# Ask the user to choose a letter
letter = input("Choose a letter: ").strip().lower()

# Find all words beginning with the chosen letter
matching_words = [word for word in words if word.startswith(letter)]

# Print the matching words
if matching_words:
    print("Words beginning with '{}':".format(letter))
    for word in matching_words:
        print(word)
else:
    print("No words found beginning with '{}'.".format(letter))

# Print the count
print("Number of words found:", len(matching_words))