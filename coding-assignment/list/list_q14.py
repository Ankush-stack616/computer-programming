# Write a program to flatten a nested list into a single list.

nested_lst = eval(input("Enter a nested list (e.g., [[1, 2], [3, 4]]): "))
flattened = [item for sublist in nested_lst for item in sublist]
print("Flattened list:", flattened)
