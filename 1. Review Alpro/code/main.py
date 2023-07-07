import os

os.system("cls")

# mengecek bilangan ganjil atau genap
def oddEven(awal, akhir):
    ganjil, genap = [], []
    one = awal
    two = akhir
    while one <= two:
        if one % 2 == 0:
            genap.append(one)
        else:
            ganjil.append(one)
        one += 1
    return ganjil, genap


print(oddEven(1, 10))


def checkPrime(num):
    factor = 0

    for i in range(1, num + 1):
        if num % i == 0:
            factor += 1
    if factor == 2:
        return True
    else:
        return False


print(checkPrime(10))


def isPrime(num):

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def getPrimes(n):
    primes = []

    for num in range(2, n + 1):

        if isPrime(num):
            primes.append(num)

    return primes


primes = getPrimes(20)


print(primes)


def countFactorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i

    return result


def multiplyMatrix(A, B):

    # Memeriksa jumlah kolom pada A dan baris pada B
    if len(A[0]) != len(B):
        return

    # Membuat result matriks dengan ukuran
    # baris pada A dan kolom pada B
    # Hasil = [baris_A][kolom_B]
    result = [[0 for j in range(len(B[0]))] for i in range(len(A))]

    # Mulai Perulangan ke setiap elemen dimana
    # baris dari result hasil akan sama dengan
    # baris A dan Kolom dari result hasilnya sama
    # dengan Kolom dari B
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result


# Definisi Matrik A
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Definisi Matrik B
B = [[2, 0, 1], [3, 0, 0], [5, 1, 1]]

print("Hasil perkalian antara matriks dari two 3 x 3 matrix")
print(multiplyMatrix(A, B))
