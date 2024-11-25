# Write a function to count the vowels in a string.

def count_vowels(s):
    return sum(1 for char in s.lower() if char in 'aeiou')

string = input("Enter a string: ")
print("Number of vowels:", count_vowels(string))
