# This problem was asked by Google.
# Given the root of a binary search tree, and a target K, return two nodes in the tree whose sum equals K.
# For example, given the following tree and K of 20
#     10
#    /   \
#  5      15
#        /  \
#      11    15
# Return the nodes 5 and 15.

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

# Sample array
arr = [2, 3, 4, 1, 2, 5, 4, 7, 6 , 5, 4]
root = Node()
for i in arr:
    root.insert(i)
####
# The obvious method would be to perform an inorder traversal and then proceed as you would with the normal solution.
def inorder_l(root):
    ret = []
    if not root:
        return ret
    ret.extend(inorder_l(root.left))
    ret.append(root.val)
    ret.extend(inorder_l(root.right))
    return ret

def sum_exists_normal(root, s):
    arr = inorder_l(root)
    ret = []
    l = 0
    r = len(arr) - 1
    while l < r:
        if s < arr[l] + arr[r]:
            r -= 1
        elif s > arr[l] + arr[r]:
            l += 1
        else:
            ret.append((arr[l], arr[r]))
            r -= 1
            l += 1
    return ret
####

# The previous solution uses two passes (for generating inorder and for l,r traversal).

# Now that the obvious solution is out of the way, a more pythonic solution would be to
# implement generators of inorder traversals.

# The two generators implemented are for forward and reverse inorder traversals.

# At no point, is the entire traversal completed on either generator. When the two generators
# reach the point where they appear to cross each other, the function returns. This ensures
# that at most n iterations take place during this search. (over the obvious method's 2n iterations).
###
# Generator to yield contents of BST in ascending order.
def inorder(root):
    if not root:
        return
    yield from inorder(root.left)
    yield root.val
    yield from inorder(root.right)


# Generator to yield contents of BST in descending order.
def inorder_r(root):
    if not root:
        return
    yield from inorder_r(root.right)
    yield root.val
    yield from inorder_r(root.left)

# Returns all possible variations of sum.
def sum_exists(root, s):
    ret = []
    gen_l = inorder(root)
    gen_r = inorder_r(root)
    l = next(gen_l)
    r = next(gen_r)
    # Ensures that although two generators are used, the entire process uses
    # at most len(s) iterations.
    while l < r:
        # Iterate lowest value upward
        if l + r < s:
            l = next(gen_l)
        # Iterate highest value downward
        elif l + r > s:
            r = next(gen_r)
        # Store combination and move on to next possible combination
        else:
            ret.append((l, r))
            if l == r:
                break
            l = next(gen_l)
            r = next(gen_r)
    return ret


####
print(sum_exists_normal(root, 4))
print(sum_exists(root, 5))
