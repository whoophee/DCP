# This problem was asked by Microsoft.
# Let's represent an integer in a linked list format by having each node represent a digit in the number. The nodes make up the number in reversed order.
# For example, the following linked list:
# 1 -> 2 -> 3 -> 4 -> 5
# is the number 54321.
# Given two linked lists in this format, return their sum in the same linked list format.
# For example, given
# 9 -> 9
# 5 -> 2
# return 124 (99 + 25) as:
# 4 -> 2 -> 1
####
# Makeshift linked list class
class Node:
    def __init__(self, val = None, next = None):
        self.next = next
        self.val = val

# This is used only for generating the input linked lists.
# Using this for the overall solution is the naive way to solve the problem.
def get_linked_list(arr):
    ret_node = None
    for i in arr[::-1]:
        ret_node = Node(i, ret_node)
    return ret_node

def get_arr(ll):
    if not ll:
        return []
    return [ll.val] + get_arr(ll.next)

input_1 = get_linked_list([9, 9, 8])
input_2 = get_linked_list([5, 2])
####
# Recursive function call to find the sum and persist carryover to successive calls.
def linked_list_sum(list1, list2, carry = 0):
    # No more content to recurse on
    if not list1 and not list2 and not carry:
        return None

    val = 0
    next1 = None
    next2 = None

    if list1:
        val += list1.val
        next1 = list1.next

    if list2:
        val += list2.val
        next2 = list2.next

    val += carry
    val, carry = val % 10, int(val/10)
    return Node(val, linked_list_sum(next1, next2, carry))

####
output1 = linked_list_sum(input_1, input_2)
print(get_arr(output1))
