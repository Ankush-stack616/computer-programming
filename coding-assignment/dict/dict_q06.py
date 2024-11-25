# Write a function to safely access dictionary keys with a default value.

def safe_get(dictionary, key, default=None):
    return dictionary.get(key, default)

dictionary = {'name': 'John', 'age': 30}
key = input("Enter a key: ")
print("Value:", safe_get(dictionary, key, "Key not found"))
