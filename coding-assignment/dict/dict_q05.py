# Group elements of a list by their frequency using a dictionary.

arr = list(map(int, input("Enter a list of numbers: ").split()))
freq_dict = {}
for num in arr:
    freq_dict[num] = freq_dict.get(num, 0) + 1
print("Grouped by frequency:", freq_dict)
