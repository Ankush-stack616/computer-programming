# Write a program to check if one string is a rotation of another string.

s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

if len(s1) != len(s2):
    print("The strings are not rotations of each other (different lengths).")
else:
    combined = s1 + s1
    if s2 in combined:
        print("The strings are rotations of each other.")
    else:
        print("The strings are not rotations of each other.")
