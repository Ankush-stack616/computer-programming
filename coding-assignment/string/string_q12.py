# Write a program to reverse each word in a given sentence.

sentence = input("Enter a sentence: ")
words = sentence.split()
reversed_words = []

for word in words:
    reversed_words.append(word[::-1])

result = " ".join(reversed_words)
print("Reversed words sentence:", result)
