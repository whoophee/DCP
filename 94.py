# This problem was asked by Google.
# Given a binary tree of integers, find the maximum path sum between two nodes.
# The path must go through at least one node, and does not need to go through the root.
####
class Node:
    def __init__(self, val = None, left = None, right = None):
        self.left = left
        self.right = right
        self.val = val

#       1
#      / \
#     5   0
#   / \    \
#  4  3     1
n1 = Node(val = 4)
n2 = Node(val = 3)
n3 = Node(val = 1)
n4 = Node(left = n1, right = n2, val = 5)
n5 = Node(right = n3, val = 0)
s = Node(left = n4, right = n5, val = 1)
####
def _path(root):
    if not root:
        return 0, 0
    l_vert, l_vshape = _path(root.left)
    r_vert, r_vshape = _path(root.right)
    cur_vshape = l_vert + r_vert + root.val
    return max(l_vert, r_vert) + root.val, max([l_vshape, r_vshape, cur_vshape])

def max_path(root):
    return max(_path(root))
####
print(max_path(s))
