# Write a function to sort a list of numbers in ascending order.

def sort_list(lst):
    return sorted(lst)

lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Sorted list:", sort_list(lst))
