# Write a function to find the second largest number in a list.

def second_largest(lst):
    unique_sorted = sorted(set(lst), reverse=True)
    return unique_sorted[1] if len(unique_sorted) > 1 else None

lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Second largest:", second_largest(lst))
