# Count the frequency of digits in a number.

number = input("Enter a number: ")
digit_count = {}
for digit in number:
    digit_count[digit] = digit_count.get(digit, 0) + 1
print("Digit frequency:", digit_count)
