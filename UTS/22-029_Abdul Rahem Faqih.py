import os
os.system('cls')
print('220411100029')

def selectionSort(data):
    print(f'Data = {data}')
    for i in range(len(data)-1):
        minFlag = i
        for j in range(i+1, len(data)):
            if data[j] > data[minFlag]:
                minFlag = j
        data[i],data[minFlag] = data[minFlag],data[i]
        print(f'{i+1}. iterasi ke - {i+1} = {data}')
    print(f'data terurut = {data}')


data = [10,2,3,4,5,6,7,80,5,18]
selectionSort(data)