#  Write a program to find common elements between two lists.

lst1 = list(map(int, input("Enter numbers for list 1: ").split()))
lst2 = list(map(int, input("Enter numbers for list 2: ").split()))
common = list(set(lst1) & set(lst2))
print("Common elements:", common)
