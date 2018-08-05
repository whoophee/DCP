# This problem was asked by Twitter.
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
# in the tree. Assume that each node in the tree also has a pointer to its parent.
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
# It is possible to get both paths in one traversal. However, the readability
# of such a function would be highly lacking.
def path(root, node):
    if root == node:
        return [node]
    if not root:
        return []

    left_path = path(root.left, node)
    right_path = path(root.right, node)

    if left_path:
        return [root] + left_path
    if right_path:
        return [root] + right_path
    return []

# Here, semantics of the word "ancestor" is not pondered upon. It returns the
# node node itself if it is an ancestor of the other.
def LCA(root, node1, node2):
    path1 = path(root, node1)
    path2 = path(root, node2)
    i = 0
    while True:
        if i == len(path1) or i == len(path2):
            break
        if not path1[i] == path2[i]:
            break
        i += 1
    return path1[i - 1]
####
sol = LCA(root, m2, l3)
print(sol.val)
