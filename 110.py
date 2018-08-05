# This problem was asked by Facebook.
# Given a binary tree, return all paths from the root to leaves.
# For example, given the tree
#    1
#   / \
#  2   3
#     / \
#    4   5
# it should return [[1, 2], [1, 3, 4], [1, 3, 5]].
####
class Node:
    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

l1 = Node(5)
l2 = Node(3)
l3 = Node(7)
l4 = Node(4)
m1 = Node(2, l1, l2)
m2 = Node(1, l3, l4)
root = Node(6, m1, m2)
####
def paths(root):
    # if no node, it does not contribute to the path
    if not root:
        return []
    # if leaf node, return node as is
    if not root.left and not root.right:
        return [[root.val]]
    # generate paths to the left and right of current node
    p = paths(root.left) + paths(root.right)
    # prepend current value to generated paths
    p = [[root.val] + p[i] for i in range(len(p))]
    return p
####
print(paths(root))
