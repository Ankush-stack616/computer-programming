# Write a function to find the maximum element in a list.

def find_max(lst):
    return max(lst)

lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Maximum element:", find_max(lst))
