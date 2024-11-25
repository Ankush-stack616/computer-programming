# Write a function to generate all prime numbers up to n.

def generate_primes(n):
    primes = []
    for i in range(2, n+1):
        if all(i % p != 0 for p in primes):
            primes.append(i)
    return primes

n = int(input("Enter a number: "))
print("Prime numbers:", generate_primes(n))
