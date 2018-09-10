# This problem was asked by Uber.
# Implement a 2D iterator class. It will be initialized with an array of arrays, and should implement the following methods:
# •	next(): returns the next element in the array of arrays. If there are no more elements, raise an exception.
# •	has_next(): returns whether or not the iterator still has elements left.
# For example, given the input [[1, 2], [3], [], [4, 5, 6]], calling next() repeatedly should output 1, 2, 3, 4, 5, 6.
# Do not use flatten or otherwise clone the arrays. Some of the arrays can be empty.
####
class Iterator2D:
    def __iter__(self):
        for tmp_arr in self.arr:
            for x in tmp_arr:
                yield x
    def __init__(self, arr):
        self.arr = arr
####
t = Iterator2D([[1, 2], [3], [], [4, 5, 6]])
for a in t:
    print(a)
