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


tree = BinaryTree("a")
tree.insertLeft("b")
tree.insertRight("c")
tree.getLeftChild().insertRight("d")
tree.getRightChild().insertLeft("e")
tree.getRightChild().insertRight("f")


def print_tree_preorder(node, path="Root"):
    if node is not None:
        print(f"{node.getRootVal()} --> Path: {path}")
        if node.getLeftChild() is not None:
            print_tree_preorder(node.getLeftChild(), f"{path} -> Left")
        if node.getRightChild() is not None:
            print_tree_preorder(node.getRightChild(), f"{path} -> Right")
print_tree_preorder(tree)
