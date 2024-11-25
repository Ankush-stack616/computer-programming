# Input a tuple and a value, and count the occurrences of that value.

values = tuple(input("Enter tuple elements separated by spaces: ").split())
target = input("Enter the value to count: ")

count = 0
for ele in values:
    if ele == target:
        count += 1

print("Occurrences of", target, ":", count)
