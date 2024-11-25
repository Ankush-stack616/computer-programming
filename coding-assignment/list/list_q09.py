# Write a program to filter and display all odd numbers from a list.

lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
odds = [num for num in lst if num % 2 != 0]
print("Odd numbers:", odds)
