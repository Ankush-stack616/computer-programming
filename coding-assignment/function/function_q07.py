# Write a function to check if a number is an Armstrong number.

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    return sum(d ** len(digits) for d in digits) == n

num = int(input("Enter a number: "))
print("Is Armstrong number:", is_armstrong(num))
