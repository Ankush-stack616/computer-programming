# Check if a specific value exists in a tuple.

values = tuple(input("Enter tuple elements separated by spaces: ").split())
target = input("Enter the value to search for: ")

if target in values:
    print(target, "exists in the tuple.")
else:
    print(target, "does not exist in the tuple.")
