#  Write a program to check if a string contains only unique characters.

s = input("Enter a string: ")
char_set = set()

unique = True
for char in s:
    if char in char_set:
        unique = False
        break
    char_set.add(char)

if unique:
    print("The string has all unique characters.")
else:
    print("The string does not have all unique characters.")
