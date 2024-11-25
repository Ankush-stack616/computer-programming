# Write a program to remove duplicate elements from a list.

lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("List without duplicates:", list(set(lst)))
