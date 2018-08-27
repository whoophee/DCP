# This problem was asked by Uber.
# Given a tree where each edge has a weight, compute the length of the longest path in the tree.
# For example, given the following tree:
#    a
#   /|\
#  b c d
#     / \
#    e   f
#   / \
#  g   h
# and the weights: a-b: 3, a-c: 5, a-d: 8, d-e: 2, d-f: 4, e-g: 1, e-h: 1, the longest
# path would be c -> a -> d -> f, with a length of 17.
# The path does not have to pass through the root, and each node can have any amount of children.
####
# Wrapper class for the problem
class TreeNode:
    def __init__(self, *args):
        self.nexts = args

g = TreeNode()
h = TreeNode()
e = TreeNode((1, g), (1, h))
f = TreeNode()
d = TreeNode((2, e), (4, f))
b = TreeNode()
c = TreeNode()
a = TreeNode((3, b), (5, c), (8, d))
####
def _longest(root):
    # Leaf node
    if not root.nexts:
        return (0, 0)
    # Maintain the two longest paths from current node
    vertical_max = [0, 0]
    # Maintain longest possible v-shaped subpaths
    vshape_max = 0
    # Iterate over children
    for d, nxt in root.nexts:
        # Get longest path for child
        vertical_path, vshape_path = _longest(nxt)
        # Modify longest paths accordingly
        vertical_max.append(vertical_path + d)
        vertical_max.remove(min(vertical_max))
        # modify longest v-shape path accordingly
        vshape_max = max(vshape_max, vshape_path)
    # Best v-shape path is either emanates on either side of current node or previously discovered
    return max(vertical_max), max(sum(vertical_max), vshape_max)

def longest_path(root):
    return max(_longest(root))

####
print(longest_path(a))
