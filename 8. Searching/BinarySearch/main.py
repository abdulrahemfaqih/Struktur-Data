import os
os.system('cls')

def binarySearch(listData, data):
    first = 0
    last = len(listData) - 1
    found = False

    while first <= last and not found:
        midIdx = (first + last) // 2
        if listData[midIdx] == data:
            found = True
        else:
            if data < listData[midIdx]:
                last = midIdx - 1
            else:
                first = midIdx + 1
    return found

data = [1,2,3,4,5,6,8,9]
print(binarySearch(data, 6))