# Write a program to find the second largest element in a list of numbers.

lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
unique_sorted = sorted(set(lst), reverse=True)
print("Second largest:", unique_sorted[1] if len(unique_sorted) > 1 else None)
