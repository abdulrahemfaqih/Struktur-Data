import os
os.system('cls')


def createDeque():
    d = []
    return d
def addFront(d,data):
    d.insert(0,data)   
    return(d)
def addRear(d,data):
    d.append(data)
    return d
def removeFront(d):
    data = d.pop(0)
    return data
def removeRear(d):
    data = d.pop()  
    return data
def isEmpty(d):
    return d == 0
def size(d):
    return len(d)

def checkPalindrom(str):
    palindrom = createDeque()
    for char in str:
        addRear(palindrom, char)
    cek = True
    while size(palindrom) > 1:
        a = removeRear(palindrom)
        b = removeFront(palindrom)
        if a == b:
            cek = cek and True
        else:
            cek = cek and False
    return cek

print(checkPalindrom('hannap'))


    
    
