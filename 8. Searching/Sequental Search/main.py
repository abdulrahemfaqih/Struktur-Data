import os
os.system('cls')    

# Unordered Sequential Search
# def unSeqSearch(listData, data):
#     idx = 0
#     found = False
#     while idx < len(listData) and not found:
#         if listData[idx] == data:
#             found = True
#         else:
#             idx += 1
#     print(f'jumlah iterasi = {idx}')
#     return found


# data = [2,3,3,2,1,4,5,7,8,5]
# print(unSeqSearch(data, 2))



# # Ordered List Sequential Search 
def orSeqSearch(listData, data):
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
hasil, jumlahIterasi = orSeqSearch(data, 5)
print(f"Posisi data = {hasil}")
print(f"Jumlah iterasi = {jumlahIterasi}")





# 