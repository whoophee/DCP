# This problem was asked by Jane Street.
# Generate a finite, but an arbitrarily large binary tree quickly in O(1).
# That is, generate() should return a tree whose size is unbounded but finite.
####
# So @property is a thing in python. The tree is lazily evaluated every step of the way.
# The creation does not happen until you try and access the property.
####
class Node:
    def __init__(self, val = 0):
        self.val = val
        self._left = None
        self._right = None

    @property
    def left(self):
        if not self._left:
            self._left = Node()
        return self._left

    @property
    def right(self):
        if not self._right:
            self._right = Node()
        return self._right

def generate():
    return Node()
