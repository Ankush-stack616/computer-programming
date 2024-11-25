# Reverse keys and values in a dictionary.

dictionary = {'a': 1, 'b': 2, 'c': 3}
reversed_dict = {v: k for k, v in dictionary.items()}
print("Reversed dictionary:", reversed_dict)
