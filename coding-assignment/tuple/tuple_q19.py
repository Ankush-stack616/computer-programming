# Input two tuples and find the common elements.

tuple1 = tuple(input("Enter elements of the first tuple separated by spaces: ").split())
tuple2 = tuple(input("Enter elements of the second tuple separated by spaces: ").split())

common_elements = set(tuple1).intersection(tuple2)
print("Common Elements:", tuple(common_elements))
