import os
os.system('cls')
def customOrSeqSearch(listData, data):
    positions = []
    iterations = 0
    idx = 0
    stop = False
    while idx < len(listData) and  not stop:
        iterations += 1
        if listData[idx] == data:
            positions.append(idx)
        else:
            if listData[idx] > data:
                stop = True
        idx += 1
    
    if positions:
        return positions, iterations
    else:
        return 'Data tidak ada', iterations

data = [1, 1, 5, 5, 5, 8, 9, 10, 12, 26]
hasil, jumlahIterasi = customOrSeqSearch(data, 5)
print(f"Posisi data = {hasil}")
print(f"Jumlah iterasi = {jumlahIterasi}")
