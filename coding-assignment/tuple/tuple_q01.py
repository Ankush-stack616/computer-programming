#  Take multiple inputs from the user and store them in a tuple, then print the tuple.

n = int(input("Enter the number of elements: "))
elements = []

for i in range(n):
    ele = input(f"Enter element {i+1}: ")
    elements.append(ele)

result_tuple = tuple(elements)
print("Created Tuple:", result_tuple)
