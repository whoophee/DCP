# This problem was asked by Google.
# Given an array of integers, return a new array where each element in the new array
# is the number of smaller elements to the right of that element in the original input array.
# For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:
# •	There is 1 smaller element to the right of 3
# •	There is 1 smaller element to the right of 4
# •	There are 2 smaller elements to the right of 9
# •	There is 1 smaller element to the right of 6
# •	There are no smaller elements to the right of 1
####
class Node:
    def insert(self, val, ctr = 0):
        if not self.val:
            self.val = val
            return ctr
        if val < self.val:
            if not self.left:
                self.left = Node()
            return self.left.insert(val, ctr)
        else:
            if not self.right:
                self.right = Node()
            # Trace the number of right sifts and element goes through.
            # This would give us the number of previously numbers it is grater than.
            return self.right.insert(val, ctr + 1)

    def __init__(self):
        self.left = None
        self.right = None
        self.val = None
        
def numbers_less_than(arr):
    root = Node()
    sol = []
    # Insert elements in reverse order. The tree is built with the intent to
    # return the appropriate counters for each element.
    for x in reversed(arr):
        sol.insert(0, root.insert(x))
    return sol
####
print(numbers_less_than([3, 4, 9, 6, 1]))
