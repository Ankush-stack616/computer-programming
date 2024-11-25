# Take a tuple as input and print the element at a specific index.

values = tuple(input("Enter tuple elements separated by spaces: ").split())
index = int(input("Enter the index you want to access: "))

if 0 <= index < len(values):
    print("Element at index", index, "is", values[index])
else:
    print("Index out of range!")
