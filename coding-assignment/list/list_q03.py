# Write a program to reverse a list of numbers and display the reversed list.

lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Reversed list:", lst[::-1])
