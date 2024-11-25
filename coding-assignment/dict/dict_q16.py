# Combine dictionaries by summing values of common keys.

from collections import Counter

dict1 = {'a': 10, 'b': 20}
dict2 = {'a': 15, 'c': 25}
combined = dict(Counter(dict1) + Counter(dict2))
print("Combined dictionary:", combined)
