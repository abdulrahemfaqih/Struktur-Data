import os
os.system('cls')
def createMatrix():
    matrix = []
    rows = int(input("Jumlah baris = "))
    columns = int(input("Jumlah kolom = "))
    for i in range(rows):
        matrix.append([])
    for i in range(rows):
        for j in range(columns):
            matrix[i].append(0)
    amountOfData = int(input("Jumlah data = "))
    for i in range(amountOfData):
        row = int(input("baris ke ? "))
        column = int(input("kolom ke ? "))
        element = int(input(f"Matrix [{row}, {column}] = "))
        matrix[row][column] = element
    print()
    print(matrix)
    return matrix

createMatrix()


def printSparseMatrix(matrix):
    for row in matrix:
        elements = "  ".join([str(element) for element in row])
        print(f"| {elements} |")
        

def multiplyMatrix(matrix1, matrix2):
    result = []
    if len(matrix1[0]) != len(matrix2):
        print("\njumlah kolom pada matrix1 harus sama dengan jumlah baris pada matrix2 ")
    else:
        for row in range(len(matrix1)):
            resultRow = []
            for column in range(len(matrix2[0])):
                sum = 0
                for i in range(len(matrix2)):
                    sum += matrix1[row][i] * matrix2[i][column]
                resultRow.append(sum)
            result.append(resultRow)
    return result




