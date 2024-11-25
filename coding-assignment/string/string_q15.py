# Write a program to compress a string by replacing consecutive occurrences of the same character with the character followed by the count.

s = input("Enter a string: ")
compressed = ""
count = 1

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        compressed += s[i-1] + str(count)
        count = 1

compressed += s[-1] + str(count)  
print("Compressed string:", compressed)
