import os
os.system("cls")

def remainderFunction(data, num):
    return data%num

def createHashTable(num):
    temp = []
    for i in range(num):
        temp.append([None])
    return temp


def chaining(data, table):
    for i in range(len(data)):
        idx = remainderFunction(data[i], len(table))
        if table[idx][0] is None:
            table[idx][0] = data[i]
        else:
            table[idx].append(data[i])
    return table

def searchHash(data, table):
    hashValue = remainderFunction(data, len(table))
    if data in table[hashValue]:
        slot = hashValue
        slotValue = table[slot]
        for index in range(len(slotValue)):
            if slotValue[index] == data:
                return f"data berada pada slot ke - {slot} dan indeks ke - {index}"
    else:
        return False

data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
hashTable = createHashTable(11)
print(chaining(data, hashTable))
print(searchHash(66, hashTable))
print(searchHash(54, hashTable))
print(searchHash(20, hashTable))
print(searchHash(55, hashTable))
print(searchHash(100, hashTable))



        



