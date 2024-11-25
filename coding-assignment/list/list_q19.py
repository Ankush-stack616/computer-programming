# Write a program to compute the cumulative sum of a list.

lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
cumulative_sum = []
total = 0
for num in lst:
    total += num
    cumulative_sum.append(total)
print("Cumulative sum:", cumulative_sum)
