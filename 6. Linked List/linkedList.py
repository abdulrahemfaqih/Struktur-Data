import os
os.system('cls')

class Node:
    def __init__(self, init__data):
        self.data = init__data
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self, newData):
        self.data = newData
    def setNext(self, newNext):
        self.next = newNext

class linkedList:
    def __init__(self):
        self.head = None
    def add(self, item):        
        temp = Node(item)        
        temp.setNext(self.head)        
        self.head = temp
    def display(self):
        current = self.head
        while current != None:
            print(current.getData())
            current = current.getNext()
    def insertPrevious(self, item, target):
        current = self.head
        previous = None
        found = False
        while current != None and not found:
            if current.getData() == target:
                found = True
            else:
                previous = current
                current = current.getNext()
        if found:
            temp = Node(item)
            if previous == None:
                temp.setNext(self.head)
                self.head = temp
            else:
                temp.setNext(current)
                previous.setNext(temp)
        else:
            print("Target not found in linked list")

# [10] -[]- [30] - [50]
myList = linkedList()
myList.add(50)
myList.add(30)
myList.add(10)
print('Lindked list sebelum di insert Previous    ')
myList.display()
myList.insertPrevious(20,30) # node baru dengan nilai 20 ditambahkan sebelum node dengan nilai 30
myList.insertPrevious(40,50) # node baru dengan nilai 40 ditambahkan sebelum node dengan nilai 50
print('Lindked list setelah di insert Previous')
myList.display()