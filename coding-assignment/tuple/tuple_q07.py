# Create a tuple of integers and find the minimum and maximum values.

values = tuple(map(int, input("Enter integers separated by spaces: ").split()))

if len(values) > 0:
    print("Minimum value:", min(values))
    print("Maximum value:", max(values))
else:
    print("The tuple is empty.")
