import os

os.system("cls")


# 1. ascending tapi dari belakang
def insertionSortAsc(arr):
    n = len(arr)
    iterasi = 1
    for i in range(n - 2, -1, -1):
        key = arr[i]
        print(f"iterasi {iterasi}")
        print(f'key = {key}')
        iterasi += 1
        j = i + 1
        while j < n and key > arr[j]:
            arr[j - 1] = arr[j]
            j += 1
        arr[j - 1] = key
        print(arr)

array = [9, 5, 1, 4, 3]
print("Array sebelum diurutkan:", array)
insertionSortAsc(array)
print("Array setelah diurutkan:", array)


# 2. descending tapi dari belakang
print("\n")


def insertionSortAsc(arr):
    n = len(arr)
    iterasi = 1
    for i in range(n - 2, -1, -1):
        key = arr[i]
        print(f"iterasi {iterasi}")
        print(f'key = {key}')
        iterasi += 1
        j = i + 1
        while j < n and key < arr[j]:
            arr[j - 1] = arr[j]
            j += 1
        arr[j - 1] = key
        print(arr)


# Contoh penggunaan
array = [9, 5, 1, 4, 3]
print("Array sebelum diurutkan:", array)
insertionSortAsc(array)
print("Array setelah diurutkan:", array)
