# Find all unique characters in a string using a dictionary.

string = input("Enter a string: ")
char_count = {}
for char in string:
    char_count[char] = char_count.get(char, 0) + 1
unique_chars = [k for k, v in char_count.items() if v == 1]
print("Unique characters:", unique_chars)
