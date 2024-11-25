# Write a program to count the frequency of each character in a string.

s = input("Enter a string: ")
char_count = {}

for char in s:
    char_count[char] = char_count.get(char, 0) + 1

print("Character frequencies:")
for char, count in char_count.items():
    print(f"{char}: {count}")
