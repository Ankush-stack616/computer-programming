# Write a program to input a list and find the index of a specific element.

lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
x = int(input("Enter the element to find: "))
print("Index:", lst.index(x) if x in lst else -1)
