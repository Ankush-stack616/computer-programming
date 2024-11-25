# Write a program to input a list and display the frequency of each element in it.

lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
freq = {}
for num in lst:
    freq[num] = freq.get(num, 0) + 1
print("Frequency:", freq)
