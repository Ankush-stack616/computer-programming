# Write a function to find the HCF and LCM of two numbers.

def hcf_and_lcm(a, b):
    hcf = gcd(a, b)
    lcm = abs(a * b) // hcf
    return hcf, lcm

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
hcf, lcm = hcf_and_lcm(a, b)
print("HCF:", hcf, "LCM:", lcm)
