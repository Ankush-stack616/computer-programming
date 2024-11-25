# Write a function to count the frequency of each element in a list.

def count_frequency(lst):
    freq = {}
    for num in lst:
        freq[num] = freq.get(num, 0) + 1
    return freq

lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Frequency count:", count_frequency(lst))
