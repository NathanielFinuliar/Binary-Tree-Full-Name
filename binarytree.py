# Coded by: Nathaniel Finuliar

class BinaryTreeNode():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # Add child to the parent class
    def add_child(self, data):
        if(data == self.data):
            return
        elif(data < self.data):
            if(self.left):
                self.left.add_child(data)
            else:
                self.left = BinaryTreeNode(data)
        else:
            if(self.right):
                self.right.add_child(data)
            else:
                self.right = BinaryTreeNode(data)
