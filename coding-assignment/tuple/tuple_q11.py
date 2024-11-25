#  Unpack the elements of a tuple into individual variables.

values = tuple(input("Enter tuple elements separated by spaces: ").split())

if len(values) >= 3:
    a, b, c = values[0], values[1], values[2]
    print("First element:", a)
    print("Second element:", b)
    print("Third element:", c)
else:
    print("Tuple does not have enough elements to unpack!")
