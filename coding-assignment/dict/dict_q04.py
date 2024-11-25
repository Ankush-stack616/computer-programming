# Find the top N most frequent elements in a list.

from collections import Counter

arr = list(map(int, input("Enter a list of numbers: ").split()))
n = int(input("Enter the value of N: "))
freq = Counter(arr)
top_n = freq.most_common(n)
print("Top N frequent elements:", top_n)
