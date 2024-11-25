# Write a function to merge two dictionaries.

def merge_dicts(dict1, dict2):
    return {**dict1, **dict2}

dict1 = eval(input("Enter the first dictionary: "))
dict2 = eval(input("Enter the second dictionary: "))
print("Merged dictionary:", merge_dicts(dict1, dict2))

