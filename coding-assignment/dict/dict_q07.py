# Check if one dictionary is a subset of another.

dict1 = eval(input("Enter the first dictionary: "))
dict2 = eval(input("Enter the second dictionary: "))
is_subset = all(item in dict2.items() for item in dict1.items())
print("Is subset:", is_subset)
