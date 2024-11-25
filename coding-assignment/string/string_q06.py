# Write a program to check if two strings are anagrams.

s1 = input("Enter the first string: ").lower()
s2 = input("Enter the second string: ").lower()

if len(s1) != len(s2):
    print("The strings are not anagrams (length mismatch).")
else:
    sorted_s1 = sorted(s1)
    sorted_s2 = sorted(s2)
    if sorted_s1 == sorted_s2:
        print("The strings are anagrams!")
    else:
        print("The strings are not anagrams.")
