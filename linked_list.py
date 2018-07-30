# Makeshift linked list class
class Node:
    def __init__(self, val = None, next = None):
        self.next = next
        self.val = val

def get_linked_list(arr):
    ret_node = None
    for i in arr[::-1]:
        ret_node = Node(i, ret_node)
    return ret_node

def get_arr(ll):
    if not ll:
        return []
    return [ll.val] + get_arr(ll.next)
