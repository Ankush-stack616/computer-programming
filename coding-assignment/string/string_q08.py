# Write a program to count words of a specific length in a sentence.

sentence = input("Enter a sentence: ")
length = int(input("Enter the word length to count: "))

words = sentence.split()
count = 0

for word in words:
    if len(word) == length:
        count += 1

print(f"Number of words of length {length}: {count}")
