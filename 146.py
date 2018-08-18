# This question was asked by BufferBox.
# Given a binary tree where all nodes are either 0 or 1, prune the tree so that
# subtrees containing all 0s are removed.
# For example, given the following tree:
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  0   0
# should be pruned to:
#    0
#   / \
#  1   0
#     /
#    1
# We do not remove the tree at the root or its left child because it still has a 1 as a descendant.
####
# Makeshift tree
class Node:
    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
ln1 = Node(1)
ln2 = Node(0)
ln3 = Node(0)
ln4 = Node(0)
n1 = Node(1, ln2, ln3)
n2 = Node(0, n1, ln4)
root = Node(0, ln1, n2)
####
# This is a fairly simple tree traversal question.
# The function returns the root (should it be required), but the return is rendered
# moot by the in-place pruning.
def prune_zeros(root):
    if not root:
        return None
    left = prune_zeros(root.left)
    right = prune_zeros(root.right)
    # If the current node has a left subtree, a right subtree, or has a value of 0,
    # it needs to be preserved.
    if left or right or root.val:
        root.left = left
        root.right = right
        return root
    return None
####
prune_zeros(root)
# print(root.val)
# print(root.left.val)
# print(root.left.left, root.left.right)
# print(root.right.val)
# print(root.right.left.val)
# print(root.right.left.left)
# print(root.right.left.right)
# print(root.right.right)
