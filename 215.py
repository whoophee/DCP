# This problem was asked by Yelp.
# The horizontal distance of a binary tree node describes how far left or right the
# node will be when the tree is printed out.
# More rigorously, we can define it as follows:
# •	The horizontal distance of the root is 0.
# •	The horizontal distance of a left child is hd(parent) - 1.
# •	The horizontal distance of a right child is hd(parent) + 1.
# For example, for the following tree, hd(1) = -2, and hd(6) = 0.
#              5
#           /     \
#         3         7
#       /  \      /   \
#     1     4    6     9
#    /                /
#   0                8
# The bottom view of a tree, then, consists of the lowest node at each horizontal
# distance. If there are two nodes at the same depth and horizontal distance, either is acceptable.
# For this tree, for example, the bottom view could be [0, 1, 3, 6, 8, 9].
# Given the root to a binary tree, return its bottom view.
####
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

root = Node()
for i in [5, 3, 7, 1, 4, 6, 9, 0, 8]:
    root.insert(i)
####
def bottom_view(root):
    # Maintains current bottom view
    bottom_view = {}
    # A queue to perform BFS on the tree
    q = [(root, 0)]
    # get maximum and minimum horizontal distance for later use
    min_horiz, max_horiz = 0, 0

    while q:
        cur_node, cur_horiz = q.pop(0)
        # Since BFS is performed, nodes deeper in the tree always appear later
        bottom_view[cur_horiz] = cur_node
        
        max_horiz = max(cur_horiz, max_horiz)
        min_horiz = min(cur_horiz, min_horiz)

        # add to BFS queue
        if cur_node.left:
            q.append((cur_node.left, cur_horiz-1))
        if cur_node.right:
            q.append((cur_node.right, cur_horiz+1))
    
    ret = []
    for i in range(min_horiz, max_horiz+1):
        ret.append(bottom_view[i].val)
    return ret
####
print(bottom_view(root))
