# Write a function to find the missing number in a sequence.

def find_missing(lst, n):
    return sum(range(1, n+1)) - sum(lst)

lst = list(map(int, input("Enter the sequence with one missing number: ").split()))
n = int(input("Enter the expected size of the sequence: "))
print("Missing number:", find_missing(lst, n))
