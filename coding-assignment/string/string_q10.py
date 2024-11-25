# Write a program to count the number of uppercase and lowercase letters in a string.

s = input("Enter a string: ")

uppercase_count = 0
lowercase_count = 0

for char in s:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1

print(f"Uppercase letters: {uppercase_count}")
print(f"Lowercase letters: {lowercase_count}")
