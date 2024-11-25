# Write a program to count the frequency of words in a given string.
string = input("Enter a string: ")
words = string.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print("Word frequency:", word_count)
