# Good morning! Here's your coding interview problem for today.
# This problem was asked by Amazon.
# Given a node in a binary tree, return the next bigger element, also known as the inorder successor.
# For example, the inorder successor of 22 is 30.
#    10
#   /  \
#  5    30
#      /  \
#    22    35
# You can assume each node has a parent pointer.
####
# makeshift binary tree with parents for given problem
class BTreeNode:
    def add_node(self, val, parent = None):
        if not self.val:
            self.val = val
            self.parent = parent
            return

        modify_node = None
        if val < self.val:
            if not self.left:
                self.left = BTreeNode()
            modify_node = self.left
        else:
            if not self.right:
                self.right = BTreeNode()
            modify_node = self.right

        modify_node.add_node(val, self)

    def __init__(self):
        self.val = None
        self.parent = None
        self.right = None
        self.left = None

def create_tree(arr):
    temp = BTreeNode()
    for a in arr:
        temp.add_node(a)
    return temp

def node_by_value(val, subtree):
    if not subtree:
        return None
    if subtree.val < val:
        return node_by_value(val, subtree.right)
    elif subtree.val > val:
        return node_by_value(val, subtree.left)
    else:
        return subtree
####
def get_parent(node):
    if not node.parent:
        return None, False
    # returns parent and whether the parent is to the right of the given node
    return node.parent, node.parent.left == node

def inorder_successor(node):
    cur_node = node
    # if it has a right child, just return
    if cur_node.right:
        return cur_node.right
    # if not, traverse parents
    while True:
        parent_node, is_right_parent = get_parent(cur_node)
        # no more parents left to traverse
        if not parent_node:
            return None
        if is_right_parent:
            return parent_node
        else:
            cur_node = parent_node
####
tree = create_tree([10, 5, 30, 22, 35])
input_node = node_by_value(22, tree)
sol = inorder_successor(input_node)
print(sol.val)
