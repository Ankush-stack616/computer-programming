# Write a program to find the longest palindromic substring in a string.

s = input("Enter a string: ")

def is_palindrome(substring):
    return substring == substring[::-1]

longest = ""
n = len(s)

for i in range(n):
    for j in range(i, n):
        substring = s[i:j+1]
        if is_palindrome(substring) and len(substring) > len(longest):
            longest = substring

print("Longest palindromic substring:", longest)
