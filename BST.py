# BST rudimentary definition
class Node:
    def insert(self, val):
        if not self.val:
            self.val = val
            return
        if val < self.val:
            if not self.left:
                self.left = Node()
            self.left.insert(val)
        else:
            if not self.right:
                self.right = Node()
            self.right.insert(val)

    def __init__(self):
        self.left = None
        self.right = None
        self.val = None
