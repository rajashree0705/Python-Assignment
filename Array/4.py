rows = int(input("Rows: "))
cols = int(input("Columns: "))
print("Enter first matrix:")
matrix1 = [list(map(int, input().split())) for _ in range(rows)]
print("Enter second matrix:")
matrix2 = [list(map(int, input().split())) for _ in range(rows)]
print("Sum of matrices:")
for i in range(rows):
    for j in range(cols):
        print(matrix1[i][j] + matrix2[i][j], end=" ")
    print()
