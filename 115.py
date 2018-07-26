# This problem was asked by Google.
# Given two non-empty binary trees s and t, check whether tree t has exactly the
# same structure and node values with a subtree of s. A subtree of s is a tree
# consists of a node in s and all of this node's descendants. The tree s could also
# be considered as a subtree of itself.
####
# Once an inorder traversal is performed on both trees, it becomes a substring search problem.
def DFS(root):
    ret = []
    if not root:
        return ret
    ret
