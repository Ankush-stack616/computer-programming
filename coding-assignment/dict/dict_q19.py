# Remove keys with None or empty values from a dictionary.

dictionary = {'a': 1, 'b': None, 'c': '', 'd': 3}
filtered_dict = {k: v for k, v in dictionary.items() if v}
print("Filtered dictionary:", filtered_dict)
