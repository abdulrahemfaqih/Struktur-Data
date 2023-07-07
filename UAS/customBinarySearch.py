# 220411100029
def customBinarySearch(listData, data):
    first = 0
    last = len(listData) - 1
    position = []
    iterations = 0
    stop = False
    while first <= last and not stop:
        iterations += 1
        midPoint = (first + last) // 2
        if listData[midPoint] == data:
            position.append(midPoint)
            if listData[midPoint + 1] == data:
                first = midPoint + 1
            elif listData[midPoint - 1] == data:
                last = midPoint - 1
            else:
                stop = True
        else:
            if data < listData[midPoint]:
                last = midPoint - 1
            else:
                first = midPoint + 1

    if position:
        return position, iterations
    else:
        return "Data tidak ada", iterations


data = [1, 1, 5, 5, 5, 6, 6, 6, 8, 9, 10, 12, 13, 13, 14, 15, 17, 19, 23, 23, 26]
hasil, jumlahIterasi = customBinarySearch(data, 5)
print(f"Posisi data = {hasil}")
print(f"Jumlah iterasi = {jumlahIterasi}")
print("\n")
hasil, jumlahIterasi = customBinarySearch(data, 18)
print(f"Posisi data = {hasil}")
print(f"Jumlah iterasi = {jumlahIterasi}")
print("\n")
hasil, jumlahIterasi = customBinarySearch(data, 13)
print(f"Posisi data = {hasil}")
print(f"Jumlah iterasi = {jumlahIterasi}")
print("\n")
