import os

os.system("cls")


def insertionSort(Data):
    print(f'data = {data}')
    for i in range(1, len(Data)):
        key = data[i]
        print(f'key = {key}')
        j = i - 1
        while j >= 0 and key <= Data[j]:
            data[j + 1] = data[j]
            j -= 1
            print(f"    {data}")
        data[j + 1] = key
    print(f"data urut = {data}")


data = [10, 5, 7, 9]
insertionSort(data)

print('\n')


def insertionSort(data):
    print(f'data = {data}')
    for i in range(len(data) - 2, -1, -1):
        key = data[i]
        print(f'key = {key}')
        j = i + 1
        while j < len(data) and key < data[j]:
            data[j - 1] = data[j]
            j += 1
            print(f"    {data}")
        data[j - 1] = key
    print(f"data urut = {data}")

data = [10, 5, 7, 9]
insertionSort(data)


data = [10, 5, 7, 9]
insertionSort(data)







