# This problem was asked by Google.
# Determine whether a doubly linked list is a palindrome. What if it’s singly linked?
# For example, 1 -> 4 -> 3 -> 4 -> 1 returns true while 1 -> 4 returns false.
class Node:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class DoublyLinked:
    def add(self, val):
        tmp = Node(val)
        if not self.top:
            self.top = self.bottom = tmp
        else:
            self.top.right = tmp
            tmp.left = self.top
            self.top = tmp

    def __init__(self):
        self.top = None
        self.bottom = None

p = DoublyLinked()
for x in [1, 4, 3, 4, 1]:
    p.add(x)

q = DoublyLinked()
for x in [1, 4, 3]:
    q.add(x)
####
# Short of transforming said linked list to an array, any other solution would be
# too convoluted and would gain at most O(n) space efficiency. Even this tradeoff
# would be gained by modifying the original linked list in-place in linear time.
def check_palindrome(ll):
    tmp = []
    cur = ll.bottom
    while cur:
        tmp.append(cur.val)
        cur = cur.right
    beg = 0
    end = len(tmp) - 1
    while beg < end:
        if tmp[beg] != tmp[end]:
            return False
        beg += 1
        end -= 1
    return True
####
print(check_palindrome(p))
print(check_palindrome(q))
