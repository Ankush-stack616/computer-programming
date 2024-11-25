# Filter out keys starting with a specific character.

dictionary = {'apple': 1, 'banana': 2, 'cherry': 3, 'apricot': 4}
start = input("Enter starting character: ")
filtered_dict = {k: v for k, v in dictionary.items() if not k.startswith(start)}
print("Filtered dictionary:", filtered_dict)
