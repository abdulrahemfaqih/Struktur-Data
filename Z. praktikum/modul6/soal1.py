import os
os.system('cls')    

def customUnSeqSearch(listData, data):
    posisiData = []
    idx = 0
    iterations = 0
    while idx < len(listData):
        iterations += 1
        if listData[idx] == data:
            posisiData.append(idx)
        idx += 1
    if posisiData:
        return posisiData, iterations
    else:
        return 'Data tidak ada', iterations


data = [1, 5, 9, 8, 1, 5, 10, 26, 5, 12]
hasil, jumlahIterasi = customUnSeqSearch(data, 1)
print(f'Posisi data = {hasil}')
print(f'Jumlah iterasi = {jumlahIterasi}')
print()
data = [1, 5, 9, 8, 1, 5, 10, 26, 5, 12]
hasil, jumlahIterasi = customUnSeqSearch(data, 13)
print(f'Posisi data = {hasil}')
print(f'Jumlah iterasi = {jumlahIterasi}')

