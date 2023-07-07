import os
os.system("cls")


def customSelectionSort(data):
    print('algoritma modifikasi Selection Sort')
    print(f'data awal = {data}')
    lenData = len(data)
    # count = 1
    for i in range(lenData // 2):
        min_flag = i
        print(f'iterasi ke - {i + 1}')
        for j in range(min_flag, lenData):
            if data[min_flag] > data[j]:
                min_flag = j
        data[i], data[min_flag] = data[min_flag], data[i]
        print(f"urut data minimal  : {data} ")
        max_flag = lenData - 1
        for j in range(lenData - 1, i, -1):
            if data[max_flag] < data[j]:
                max_flag = j
        data[lenData - 1], data[max_flag] = data[max_flag], data[lenData - 1]
        print(f"urut data maksimal : {data} ")
        lenData -= 1
    print(f'data urut = {data}')

data = [10, 2, 5, 8, 1, 20, 7, 12, 4]
customSelectionSort(data)

