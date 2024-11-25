# Write a function to print the first n Fibonacci numbers.

def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

num = int(input("Enter the number of terms: "))
print("Fibonacci series:", fibonacci(num))
