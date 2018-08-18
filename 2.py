# This problem was asked by Uber.
# Given an array of integers, return a new array such that each element at index i
# of the new array is the product of all the numbers in the original array except
# the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be
# [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be
# [2, 3, 6].
# Follow-up: what if you can't use division?
####
def leaveoneout(arr):
    asc = [1]
    desc = [1]
    n = len(arr)
    # generate product in forward and backward order
    for i in range(n):
        asc.append(asc[-1] * arr[i])
        desc.append(desc[-1] * arr[n-i-1])
    ret = []
    # calculate leave-out product
    for i in range(n):
        ret.append(asc[i] * desc[n-i-1])
    return ret
####
print(leaveoneout([1, 2, 3, 4, 5]))
