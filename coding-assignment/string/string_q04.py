# Write a program to find the frequency of each character in a string.

s = input("Enter a string: ")
freq = {}
for char in s:
    freq[char] = freq.get(char, 0) + 1
print("Character frequencies:", freq)
