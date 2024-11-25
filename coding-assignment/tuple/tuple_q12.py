# Input a tuple of integers and find the sum of its elements.

values = tuple(map(int, input("Enter integers separated by spaces: ").split()))
total = 0

for num in values:
    total += num

print("Sum of tuple elements:", total)
