# Create a dictionary from two lists (keys and values).

keys = input("Enter keys separated by spaces: ").split()
values = input("Enter values separated by spaces: ").split()
dictionary = dict(zip(keys, values))
print("Dictionary:", dictionary)
