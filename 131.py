# This question was asked by Snapchat.
# Given the head to a singly linked list, where each node also has a “random”
# pointer that points to anywhere in the linked list, deep clone the list.
####
# The pythonic way to uniquely identify objects is done using the id() built-in
# Solving this problem in another language could either use the reference to the
# memory address to uniquely identify objects or write a hash function specific
# to the object.
#
# Sample linked list:
# a -> b -> c
# Random links:
# a -> c
# b -> a
# c -> b
####
# Makeshift class for this problem
class LinkedList:
    def deepcopy(self):
        return LinkedList(self.val)
    def __init__(self, val = None, next = None, rand_link = None):
        self.val = val
        self.next = next
        self.rand_link = rand_link

c = LinkedList(5)
b = LinkedList(4, c)
a = LinkedList(3, b, c)
c.rand_link = b
b.rand_link = a

def describe_list(root):
    while root:
        print("{} || val: {} | next: {} | rand: {}".format(id(root), root.val, id(root.next), id(root.rand_link)))
        root = root.next
    print("{} || None".format(id(None)))
####
def ll_deepcopy(root):
    node_map = {}
    cur_node = root
    ret = id(root)
    # generate and store deepcopies and links of each node
    while cur_node:
        cur_id = id(cur_node)
        node_map[cur_id] = (cur_node.deepcopy(), id(cur_node.next), id(cur_node.rand_link))
        cur_node = cur_node.next

    node_map[id(None)] = (None, None, None)
    # establish links in deepcopy
    for key, (node, next_id, rand_id) in node_map.items():
        if not node:
            continue
        node.next = node_map[next_id][0]
        node.rand_link = node_map[rand_id][0]

    return node_map[ret][0]
####
# notice how the contents and links are the same, but memory references are completely different
describe_list(a)
print()
describe_list(ll_deepcopy(a))
