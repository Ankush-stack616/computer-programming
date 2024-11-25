# Convert all keys of a dictionary to uppercase.

dictionary = {'name': 'Alice', 'age': 30}
uppercase_dict = {k.upper(): v for k, v in dictionary.items()}
print("Uppercase dictionary:", uppercase_dict)
