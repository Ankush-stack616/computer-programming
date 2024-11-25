# Write a program to filter and display all even numbers from a list.

lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
evens = [num for num in lst if num % 2 == 0]
print("Even numbers:", evens)
