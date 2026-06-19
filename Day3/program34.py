rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))
matrix1 = []
print("Enter Matrix 1 elements:")
for i in range(rows):
    row = [int(input()) for j in range(cols)]
    matrix1.append(row)
matrix2 = []
print("Enter Matrix 2 elements:")
for i in range(rows):
    row = [int(input()) for j in range(cols)]
    matrix2.append(row)
result = [[0 for _ in range(cols)] for _ in range(rows)]
for i in range(rows):
    for j in range(cols):
        for k in range(cols):
            result[i][j] += matrix1[i][k] * matrix2[k][j]
print("Result:")
for row in result:
    print(row)