# Write a program to calculate the product of all elements in a list.

from functools import reduce
lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
product = reduce(lambda x, y: x * y, lst)
print("Product of elements:", product)
