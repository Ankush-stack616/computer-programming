# Write a program to count all substrings that start and end with the same character.

s = input("Enter a string: ")
n = len(s)
count = 0

for i in range(n):
    for j in range(i, n):
        if s[i] == s[j]:
            count += 1

print("Number of substrings starting and ending with the same character:", count)
