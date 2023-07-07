import os
os.system('cls')
def remainderFucntion(data, num):
    return data % num

def createTable(num):
    temp = []
    for i in range(num):
        temp.append('None')
    return temp

def putData(data, table):
    for i in range(len(data)):
        idx = remainderFucntion(data[i], len(table))
        table[idx] = data[i]
    return table

def searchHash(data, table):
    hashValue = remainderFucntion(data, len(data))
    if data == table[hashValue]:
        return True
    else:
        return False
    

data = [4,5,6,8,3,2,1]

hashTable = createTable(11)
print(hashTable)
hashTable = putData(data, hashTable)
print(hashTable)