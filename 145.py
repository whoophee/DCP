# This problem was asked by Google.
# Given the head of a singly linked list, swap every two nodes and return its head.
# For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.
####
# Makeshift linked list class
class Node:
    def __init__(self, val = None, next = None):
        self.next = next
        self.val = val
root = Node(1, Node(2, Node(3, Node(4, Node(5)))))
####
def link_swap(root):
    # The linked list ends here
    if not root:
        return None
    # Odd node
    if not root.next:
        return root
    # Swap succeeding nodes
    nn = link_swap(root.next.next)

    # swap current nodes
    root.next.next = root
    ret, root.next = root.next, nn

    return ret

def ll_array(root):
    if not root:
        return []
    return [root.val] + ll_array(root.next)
####
print(ll_array(root))
print(ll_array(link_swap(root)))
