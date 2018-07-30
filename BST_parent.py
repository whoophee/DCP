# makeshift binary tree with parents for problems
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
