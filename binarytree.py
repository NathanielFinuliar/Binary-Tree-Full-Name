# Final Commit
# Coded by: Nathaniel Finuliar
# BSCOE 2-2

class BinaryTreeNode():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # Add child to the parent class
    def add_child(self, data):
        if(data == self.data):
            return
        
        #Goes to left subtree (if data is < the value of current node)
        elif(data < self.data):
            if(self.left):
                self.left.add_child(data)
            else:
                self.left = BinaryTreeNode(data)

        #Goes to right subtree (if data is > the value of current node)
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

    #Delete function for Exercise 2
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

if(__name__=="__main__"):
    symbol = "_"
    fullname = list("NathanielDFinuliar".upper())
    name_tree = BinaryTreeNode(fullname[0])
    for num in range(1, len(fullname)):
        name_tree.add_child(fullname[num])

    print(f"\nFULL NAME:\n{fullname}")
    print(f"\nIn Order Traversal:\t{name_tree.in_order()}")
    print(f"Pre Order Traversal:\t{name_tree.pre_order()}")
    print(f"Post Order Traversal:\t{name_tree.post_order()}")
    print("\nMin Letter:",name_tree.min())
    print("Max Letter:",name_tree.max())

    letters_in = []
    letters_not = []
    alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
    for letter in alphabet:
        if(name_tree.search(letter)):
            letters_in.append(letter)
        else:
            letters_not.append(letter)

    print(f"\n{symbol*(3**4)}\n\nUsing name_tree search function to find letters that are in and not in my name\n")
    print("Letters in my name (True):\t",letters_in)
    print("Letters not in my name (False):\t",letters_not)
    print(symbol*(3**4),'\n')

    for item in name_tree.in_order():
        name_tree.delete(item)
        print(f"In Order Traversal deleted '{item}':\t{name_tree.in_order()}")

