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

    # Search for item in data
    def search(self, find):
        if(self.data == find):
            return True

        elif(find > self.data):
            if(self.right):
                return self.right.search(find)
            else:
                return False
        elif(find < self.data):
            if(self.left):
                return self.left.search(find)
            else:
                return False
    
    # In order traversal
    def in_order(self):
        items = []
        if(self.left):
            items+=self.left.in_order()

        items.append(self.data)

        if(self.right):
            items+=self.right.in_order()
        
        return items

    # Pre order traversal
    def pre_order(self):
        items = list(self.data)
        if(self.left):
            items+=self.left.pre_order()
        if(self.right):
            items+=self.right.pre_order()
        return items

    # Post order traversal
    def post_order(self):
        items = []
        if(self.left):
            items+=self.left.post_order()
        if(self.right):
            items+=self.right.post_order()
        items.append(self.data)
        return items
