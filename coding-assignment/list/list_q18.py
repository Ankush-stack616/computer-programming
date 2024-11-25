# Write a program to count the number of negative numbers in a list.

lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
negatives = sum(1 for num in lst if num < 0)
print("Count of negatives:", negatives)
