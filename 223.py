# This problem was asked by Palantir.
# Typically, an implementation of in-order traversal of a binary tree has O(h) space 
# complexity, where h is the height of the tree. Write a program to compute the in-order 
# traversal of a binary tree using O(1) space.
####
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
#       7
#      / \
#     5   1
#   / \    \
#  4  3     1
####
def morris_traversal(root):
    cur = root
    while cur:
        if not cur.left:
            print(cur.val)
            cur = cur.right
        else:
            tmp = cur.left
            while tmp.right and tmp.right != cur:
                tmp = tmp.right
            # the rightmost link has not been set yet
            if not tmp.right:
                tmp.right = cur
                cur = cur.left
            # this occurs when the rightmost link = current link
            # i.e. rightful order
            else:
                tmp.right = None
                print(cur.val)
                cur = cur.right 
####
morris_traversal(s)