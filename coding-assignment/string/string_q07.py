#  Write a program to find the first non-repeating character in a string.

s = input("Enter a string: ")
char_count = {}

for char in s:
    char_count[char] = char_count.get(char, 0) + 1

found = False
for char in s:
    if char_count[char] == 1:
        print("First non-repeating character:", char)
        found = True
        break

if not found:
    print("No non-repeating character found.")
