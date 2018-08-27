# This problem was asked by LinkedIn.
# Determine whether a tree is a valid binary search tree.
# A binary search tree is a tree with two children, left and right, and satisfies
# the constraint that the key in the left child must be less than or equal to the
# root and the key in the right child must be greater than or equal to the root.
####
class BST:
    def insert(self, val):
        if not self.val:
            self.val = val
            return
        if val < self.val:
            if not self.left:
                self.left = BST()
            self.left.insert(val)
        else:
            if not self.right:
                self.right = BST()
            self.right.insert(val)

    def __init__(self):
        self.left = None
        self.right = None
        self.val = None

btree = BST()
for x in [2, 3, 1, -1, 5, -2, 6, 4, -7]:
    btree.insert(x)

class Node:
    def __init__(self, val = None, left = None, right = None):
        self.left = left
        self.right = right
        self.val = val
n1 = Node(val = 4)
n2 = Node(val = 3)
n3 = Node(val = 1)
n4 = Node(left = n1, right = n2, val = 5)
n5 = Node(right = n3, val = 1)
s = Node(left = n4, right = n5, val = 7)
####
def is_btree(root):
    cur = root.val
    # children can either be null, or conforms to rules of BST
    l_valid = (cur > root.left.val) and is_btree(root.left) if root.left else True
    r_valid = (cur <= root.right.val) and is_btree(root.right) if root.right else True
    return l_valid and r_valid
####
print(is_btree(btree))
print(is_btree(s))
