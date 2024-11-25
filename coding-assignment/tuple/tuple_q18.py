# Convert a tuple of characters to a string.

values = tuple(input("Enter characters separated by spaces: ").split())
result_string = ''.join(values)

print("Converted String:", result_string)
