
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
    def insertPrevious(self, item, x):
        current = self.head
        previous = None
        found = False
        while current != None and not found:
            if current.getData() == x:
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
            print(" not found in linked list")

Llist = linkedList()
Llist.add(5)
Llist.add(3)
Llist.add(1)
Llist.display()
print()
Llist.insertPrevious(4,5)
Llist.insertPrevious(2,3)
Llist.display()

