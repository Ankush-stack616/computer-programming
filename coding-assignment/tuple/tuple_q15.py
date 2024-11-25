# Input a tuple of integers and sort it in ascending order.

values = tuple(map(int, input("Enter integers separated by spaces: ").split()))
sorted_tuple = tuple(sorted(values))

print("Sorted Tuple:", sorted_tuple)
