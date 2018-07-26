# This problem was asked by Facebook.
# Given a binary tree, return the level of the tree with minimum sum.
####
# Sample Tree:
#       7
#      / \
#     5   1
#   / \    \
#  4  3     1
####
class Node:
    def __init__(self, left = None, right = None, val = None):
        self.left = left
        self.right = right
        self.val = val
n1 = Node(val = 4)
n2 = Node(val = 3)
n3 = Node(val = 1)
n4 = Node(left = n1, right = n2, val = 5)
n5 = Node(right = n3, val = 1)
root = Node(left = n4, right = n5, val = 7)
####
def maxsum_level(root):
    ret = []
    q = [(root, 0)]

    while q:
        node, level = q.pop()
        try:
            ret[level] += node.val
        except IndexError:
            ret.append(node.val)

        if node.left:
            q.insert(0, (node.left, level+1))
        if node.right:
            q.insert(0, (node.right, level+1))
    return max(ret)
