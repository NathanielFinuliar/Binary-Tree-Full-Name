# CODED BY NATHANIEL D. FINULIAR
# BSCOE 2-2
# SIR DAN MADRIGALEJOS

#PROGRAM THAT APPLIES COMPUTE SUM METHOD
#WHICH CALCULATES THE SUM OF ALL ELEMENTS
#THE LIST CONTAINS NUMBERS INSTEAD OF LETTERS

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
    def in_order_traversal(self):
        items = []
        if(self.left):
            items+=self.left.in_order_traversal()

        items.append(self.data)

        if(self.right):
            items+=self.right.in_order_traversal()
        
        return items

    # Pre order traversal
    def pre_order_traversal(self):
        items = [self.data]
        if(self.left):
            items+=self.left.pre_order_traversal()
        if(self.right):
            items+=self.right.pre_order_traversal()
        return items

    # Post order traversal
    def post_order_traversal(self):
        items = []
        if(self.left):
            items+=self.left.post_order_traversal()
        if(self.right):
            items+=self.right.post_order_traversal()
        items.append(self.data)
        return items

    # Find max value
    def max(self):
        if(self.right is None):
            return self.data
        return self.right.max()

    # Find min value
    def min(self):
        if(self.left is None):
            return self.data
        return self.left.min()

    def delete(self, item):
        if(item < self.data):
            if(self.left):
                self.left = self.left.delete(item)
        elif(item > self.data):
            if(self.right):
                self.right = self.right.delete(item)
        else:
            if(self.left is None and self.right is None):
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.right

            max_val = self.left.max()
            self.data = max_val
            self.left = self.left.delete(max_val)

        return self
    
    #calculates the sum of elements
    def calculate_sum(self): 
        elements = self.in_order_traversal()
        x = 0
        for i in range(len(elements)):
            x += elements[i]
        return  x
    
def build_tree(elements): 
    main = BinaryTreeNode(elements[0])
    for i in range(1,len(elements)):
        main.add_child(elements[i])
    return main

if (__name__ == '__main__'):
    # symbol = "_"
    num_list = list(range(10,50,5))
    print("NUMBER LIST: ",num_list)
    num_list = build_tree(num_list)
    print("\nTotal sum: ",num_list.calculate_sum())
    print("\nMinimum Number: ",num_list.min())
    print("Maximum Number: ",num_list.max())
    print(f"\nIn Order Traversal:\t{num_list.in_order_traversal()}")
    print(f"Pre Order Traversal:\t{num_list.pre_order_traversal()}")
    print(f"Post Order Traversal:\t{num_list.post_order_traversal()}")
    print("_"*100)

    num_in = []
    num_not = []
    numberlist = list(range(11,50))

    for num in numberlist:
        if(num_list.search(num)):
            num_in.append(num)
        else:
            num_not.append(num)