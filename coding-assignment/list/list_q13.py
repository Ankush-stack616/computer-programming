# Write a program to calculate the median of a list of numbers.

lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
lst.sort()
n = len(lst)
print("Median:", (lst[n // 2 - 1] + lst[n // 2]) / 2 if n % 2 == 0 else lst[n // 2])
