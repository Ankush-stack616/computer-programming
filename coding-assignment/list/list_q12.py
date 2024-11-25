# Write a program to rotate a list k steps to the right.

lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
k = int(input("Enter rotation value: ")) % len(lst)
print("Rotated list:", lst[-k:] + lst[:-k])
