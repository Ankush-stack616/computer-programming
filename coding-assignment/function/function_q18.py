# Write a function to check if a number is a perfect number.

def is_perfect(n):
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

num = int(input("Enter a number: "))
print("Is perfect number:", is_perfect(num))
