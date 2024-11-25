# Write a program to input a list of numbers and find the smallest element in the list.

lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Minimum:", min(lst))
