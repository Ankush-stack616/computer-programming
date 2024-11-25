# Sort a dictionary based on the length of its keys.

dictionary = {'apple': 10, 'pear': 20, 'banana': 5}
sorted_dict = dict(sorted(dictionary.items(), key=lambda x: len(x[0])))
print("Sorted dictionary:", sorted_dict)
