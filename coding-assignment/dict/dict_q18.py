# Count the total number of keys in a nested dictionary.

def count_keys(d):
    count = len(d)
    for v in d.values():
        if isinstance(v, dict):
            count += count_keys(v)
    return count

nested_dict = {'a': 1, 'b': {'c': 2, 'd': {'e': 3}}}
print("Total number of keys:", count_keys(nested_dict))
