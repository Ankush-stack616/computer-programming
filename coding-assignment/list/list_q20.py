# Write a program to partition a list into two separate lists of even and odd numbers.

lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
evens = [num for num in lst if num % 2 == 0]
odds = [num for num in lst if num % 2 != 0]
print("Even numbers:", evens)
print("Odd numbers:", odds)
