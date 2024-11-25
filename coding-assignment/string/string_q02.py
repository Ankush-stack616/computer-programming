# Write a program to count the number of vowels and consonants in a string.

s = input("Enter a string: ").lower()
vowels = sum(1 for c in s if c in "aeiou")
consonants = sum(1 for c in s if c.isalpha() and c not in "aeiou")
print(f"Vowels: {vowels}, Consonants: {consonants}")
