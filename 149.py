# This problem was asked by Goldman Sachs.
# Given a list of numbers L, implement a method sum(i, j) which returns the sum
# from the sublist L[i:j] (including i, excluding j).
# For example, given L = [1, 2, 3, 4, 5], sum(1, 3) should return sum([2, 3]),
# which is 5.
# You can assume that you can do some pre-processing. sum() should be optimized
# over the pre-processing step.
####
class MyList(list):
    def sum(self, i, j):
        # check to see if the preprocessing has been performed
        try:
            l_sum = self._list_sum
        except AttributeError:
            l_sum = [0]
            tmp = 0
            for x in self:
                tmp += x
                l_sum.append(tmp)
            self._list_sum = l_sum
        # This is anm O(1) operation
        return l_sum[j] - l_sum[i]
####
test = MyList([1, 2, 3, 4, 5])
print(test.sum(1, 3))
print(test.sum(0, 3))
print(test.sum(0, 5))
