# This question was asked by Apple.
# Given a binary tree, find a minimum path sum from root to a leaf.
# For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.
#   10
#  /  \
# 5    5
#  \     \
#    2    1
#        /
#      -1
####
class BTree:
    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

n5 = BTree(-1)
n4 = BTree(2)
n3 = BTree(1, left = n5)
n2 = BTree(5, right = n4)
n1 = BTree(5, right = n3)
input = BTree(10, left = n2, right = n1)
####
# This is pretty self explanatory
def get_min_path(root):
    if not root:
        return 0
    return root.val + min(get_min_path(root.left), get_min_path(root.right))
####
print(get_min_path(input))
