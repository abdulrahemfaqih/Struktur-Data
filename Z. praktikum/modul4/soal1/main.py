import os

os.system("cls")


def CustomBubbleSort(data):
    lenData = len(data)
    swap = True
    print(f"data = {data}")
    while swap == True:
        swap = False
        for i in range(lenData - 1):
            if data[i] > data[i + 1]:
                swap = True
        if swap == True:
            print("Genap - Ganjil Sorting")
            for i in range(0, lenData - 1, 2):
                if data[i] > data[i + 1]:
                    data[i], data[i + 1] = data[i + 1], data[i]
            print(data)
            print("ganjil - Genap Sorting ")
            for i in range(1, lenData - 1, 2):
                if data[i] > data[i + 1]:
                    data[i], data[i + 1] = data[i + 1], data[i]
            print(data)
    return data


data = [13, 12, 10, 8, 7, 5, 11, 2]
print(CustomBubbleSort(data))
