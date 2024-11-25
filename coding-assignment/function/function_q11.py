# Write a function to generate Pascal's Triangle up to n rows.

def pascal_triangle(n):
    result = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(result[i-1][j-1] + result[i-1][j])
        row.append(1)
        result.append(row)
    return result

n = int(input("Enter number of rows: "))
triangle = pascal_triangle(n)
for row in triangle:
    print(row)
