# Write a program to capitalize the first letter of each word in a sentence.

sentence = input("Enter a sentence: ")
words = sentence.split()
capitalized_words = []

for word in words:
    capitalized_words.append(word.capitalize())

result = " ".join(capitalized_words)
print("Capitalized sentence:", result)
