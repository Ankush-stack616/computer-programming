#  Input a tuple and a value, then find the index of that value.

values = tuple(input("Enter tuple elements separated by spaces: ").split())
target = input("Enter the value to find the index of: ")

if target in values:
    index = values.index(target)
    print("Index of", target, "is", index)
else:
    print(target, "not found in the tuple.")
