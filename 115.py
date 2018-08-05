# This problem was asked by Google.
# Given two non-empty binary trees s and t, check whether tree t has exactly the
# same structure and node values with a subtree of s. A subtree of s is a tree
# consists of a node in s and all of this node's descendants. The tree s could also
# be considered as a subtree of itself.
# Example s:
#       7
#      / \
#     5   1
#   / \    \
#  4  3     1
# Example t:
# 1
#  \
#   1
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

n6 = Node(val = 1)
t1 = Node(val = 1, right = n6)
t2 = Node(val = 7, right = t1)
####
# Once an preorder traversal is performed on both trees, it becomes a substring search problem.
def preorder(root):
    if not root:
        return []
    # braces used for depth distinction
    ret = ['(']
    ret.append(root.val)
    ret.extend(preorder(root.left))
    ret.extend(preorder(root.right))
    ret.append(')')
    return ret

def KMP_preprocess(arr):
    counter = 0
    ret = [0]
    for i in range(1, len(arr)):
        if arr[counter] == arr[i]:
            counter += 1
        else:
            counter = 0
        ret.append(counter)
    return ret

# it is possible to recurse this function over all nodes in s, the inorder step
# is performed to allow KMP.
def check_subtree(s, t):
    S = preorder(s)
    T = preorder(t)
    preprocessed = KMP_preprocess(T)
    ctr = 0
    for c in S:
        while c != T[ctr] and ctr != 0:
            ctr = preprocessed[ctr - 1]
        if c == T[ctr]:
            ctr += 1

        if ctr == len(T):
            return True
    return False
####
print(check_subtree(s, n4))
print(check_subtree(s, n5))
print(check_subtree(s, t2))
