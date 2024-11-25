# Slice a tuple based on user-provided start and end indices.

values = tuple(input("Enter tuple elements separated by spaces: ").split())
start = int(input("Enter the start index: "))
end = int(input("Enter the end index: "))

if 0 <= start <= len(values) and 0 <= end <= len(values):
    sliced_tuple = values[start:end]
    print("Sliced Tuple:", sliced_tuple)
else:
    print("Invalid indices!")
