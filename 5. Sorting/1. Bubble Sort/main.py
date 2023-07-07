import os
os.system("cls")
import time

data = [13, 12, 10, 8, 7, 5, 11, 2]


def bubbleSort(data):
    print(f'data = {data}')
    for i in range(len(data)-1,0,-1):
        print(f'\niterasi luar ke-{len(data)-i} -> jumlah iterasi dalam = {i} iterasi\n')
        for j in range(i):
            if data[j] > data[j+1]:
                data[j],data[j+1] = data[j+1],data[j]
            print(f'    {j+1}. {data}')
    print(f'\ndata terurut = {data}\n')

# perhitungan waktu komputasi bubble sort
print(f'{"="*20} Bubble Sort {"="*20}')
startTime = time.time()
print(f'\nstart = {startTime}')
bubbleSort(data)
endTime = time.time()
print(f'finish = {endTime}')
BubbleSortTime = endTime - startTime

data = [13, 12, 10, 8, 7, 5, 11, 2]


def selectionSort(data):
    print(f'data = {data}\n')
    for i in range(len(data)-1):
        minFlag = i
        for j in range(i+1,len(data)):
            if data[minFlag] > data[j]:
                minFlag = j
        data[i],data[minFlag] = data[minFlag],data[i]
        print(f'{i+1}. iterasi ke - {i+1} = {data}')
    print(f'\ndata terurut = {data}\n')

# perhitungan waktu komputasi selection Sort
print(f'\n{"="*20} Selection Sort {"="*20}\n')
startTime = time.time()
print(f'start = {startTime}')
selectionSort(data)
endTime = time.time()
print(f'finish = {endTime}')
selectionSortTime = endTime - startTime

print(f'\nperbadinan waktu komputasi dari dua algoritma')
print(f'waktu komputasi algoritma bubble sort = {BubbleSortTime}')
print(f'waktu komputasi algoritma selection sort = {selectionSortTime}')

if BubbleSortTime < selectionSortTime:
    print('waktu komputasi tercepat = Algoritma Bubble Sort')
else:
    print(f'waktu komputasi tercepat = Algoritma Selection\n')
















