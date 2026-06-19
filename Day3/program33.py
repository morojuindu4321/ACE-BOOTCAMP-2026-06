rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix1 = []
print("Enter elements of Matrix 1:")
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input())
        row.append(element)
    matrix1.append(row)
matrix2 = []
print("Enter elements of Matrix 2:")
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input())
        row.append(element)
    matrix2.append(row)
result = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(matrix1[i][j] - matrix2[i][j])
    result.append(row)
print("Subtraction of Matrices:")
for row in result:
    print(row)