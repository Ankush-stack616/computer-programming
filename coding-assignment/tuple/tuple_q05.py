# Create two tuples from user input and concatenate them.

tuple1 = tuple(input("Enter elements for the first tuple separated by spaces: ").split())
tuple2 = tuple(input("Enter elements for the second tuple separated by spaces: ").split())

result_tuple = tuple1 + tuple2
print("Concatenated Tuple:", result_tuple)
