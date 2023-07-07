import os
os.system("cls")

class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key


# Membuat binary tree dengan root 'a'
tree = BinaryTree('a')

# Menambahkan left child 'b' ke root 'a'
tree.insertLeft('b')

# Menambahkan right child 'c' ke root 'a'
tree.insertRight('c')

leftChildB = tree.getLeftChild()
leftChildB.insertLeft('d')

leftChildC = tree.getLeftChild()
leftChildC.insertLeft("e")

rightChildC = tree.getRightChild()
rightChildC.insertRight("e")

# get root
# print(f"root: {tree.getRootVal()}")
# print(f"left child : {tree.getRootVal()}")





# # Menambahkan right child 'd' ke left child 'b'
# tree.getLeftChild().insertRight('d')

# # Menambahkan left child 'e' ke left child 'c'
# tree.getRightChild().insertLeft('e')

# # Menambahkan right child 'f' ke right child 'c'
# tree.getRightChild().insertRight('f')

