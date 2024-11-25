# Write a program to remove all duplicate characters from a string.

s = input("Enter a string: ")
seen = set()
result = ""

for char in s:
    if char not in seen:
        result += char
        seen.add(char)

print("String after removing duplicates:", result)
