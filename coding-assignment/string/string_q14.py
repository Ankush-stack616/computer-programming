# Write a program to find all possible substrings of a string.

s = input("Enter a string: ")

n = len(s)
substrings = []

for i in range(n):
    for j in range(i+1, n+1):
        substrings.append(s[i:j])

print("All substrings:")
for substring in substrings:
    print(substring)
