# Write a program to check if a given string is a palindrome.

s = input("Enter a string: ")
print("Palindrome" if s == s[::-1] else "Not a palindrome")
