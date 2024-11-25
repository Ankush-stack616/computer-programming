# Write a program to find elements that are unique to each of two lists.

lst1 = list(map(int, input("Enter numbers for list 1: ").split()))
lst2 = list(map(int, input("Enter numbers for list 2: ").split()))
unique = list(set(lst1) ^ set(lst2))
print("Unique elements:", unique)
