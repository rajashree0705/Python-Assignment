r1 = int(input("Enter rows for first matrix: "))
c1 = int(input("Enter columns for first matrix: "))
r2 = int(input("Enter rows for second matrix: "))
c2 = int(input("Enter columns for second matrix: "))
if c1 != r2:
    print("Matrix multiplication is not possible!")
else:
    print("Enter first matrix:")
    matrix1 = []
    for i in range(r1):
        row = []
        for j in range(c1):
            row.append(int(input(f"Element [{i}][{j}]: ")))
        matrix1.append(row)
    print("Enter second matrix:")
    matrix2 = []
    for i in range(r2):
        row = []
        for j in range(c2):
            row.append(int(input(f"Element [{i}][{j}]: ")))
        matrix2.append(row)
    result = []
    for i in range(r1):
        row = []
        for j in range(c2):
            row.append(0)
        result.append(row)
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    print("Resultant matrix:")
    for row in result:
        print(row)
