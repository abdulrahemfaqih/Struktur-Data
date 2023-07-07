from SparseMatrix import *
def main():
    print("matrix - 1 ")
    matrix1 = createMatrix()
    print("matrix - 2 ")
    matrix2 = createMatrix()
    print("matrix 1 = ")
    printSparseMatrix(matrix1)
    print("\nmatrix 2 = ")
    printSparseMatrix(matrix2)
    multiplicationMatrix = multiplyMatrix(matrix1, matrix2)
    print("\nhasil kali = ")
    printSparseMatrix(multiplicationMatrix)
main()