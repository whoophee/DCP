# This problem was asked by Apple.
# Given a tree, find the largest tree/subtree that is a BST.
# Given a tree, return the size of the largest tree/subtree that is a BST.
####
class TreeNode:
    def __init__(self, val, *args):
        self.val = val
        self.nexts = args
class BTree:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
g = TreeNode(1)
h = TreeNode(2)
i = TreeNode(3)
e = TreeNode(4, g, h, i)
f = TreeNode(5)
d = TreeNode(6, e, f)
b = TreeNode(7)
c = TreeNode(8)
a = TreeNode(9, b, c, d)
####
def _max_bst(root):
    # No node left to traverse
    if not root:
        return 0, None

    # maintain left and right branches for current node
    max_branch = [(0, None), (0, None)]
    # iterate over possible subtrees of current node
    # replace maximums if necessary
    for cur_next in root.nexts:
        max_branch.append(_max_bst(cur_next))
        max_branch.remove(min(max_branch, key = lambda x:x[0]))

    # create a binary tree node and return
    left_size, left = max_branch[0]
    right_size, right = max_branch[1]

    return (left_size + right_size + 1), BTree(root.val, left, right)

def max_btree(root):
    return _max_bst(root)[1]
def max_btree_size(root):
    return _max_bst(root)[0]
####
print(max_btree_size(a))
