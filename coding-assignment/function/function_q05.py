# Write a function to check if a string is a palindrome.

def is_palindrome(s):
    return s == s[::-1]

string = input("Enter a string: ")
print("Is palindrome:", is_palindrome(string))
