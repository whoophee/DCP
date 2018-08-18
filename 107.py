# This problem was asked by Microsoft.
# Print the nodes in a binary tree level-wise. For example, the following should
# print 7, 5, 1, 4, 3, 1
#       7
#      / \
#     5   1
#   / \    \
#  4  3     1
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
####
# Simple BFS returns the nodes in level order.
def levelwise(root):
    q = [root]
    cur = None
    while q:
        cur = q.pop(0)
        yield cur
        if cur.left:
            q.append(cur.left)
        if cur.right:
            q.append(cur.right)
####
sol = [x.val for x in levelwise(s)]
print(sol)
