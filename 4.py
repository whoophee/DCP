# This problem was asked by Stripe.
# Given an array of integers, find the first missing positive integer in linear
# time and constant space. In other words, find the lowest positive integer that
# does not exist in the array. The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# You can modify the input array in-place.
####
def lowest_skipped(arr):
    n = len(arr)

    for i in range(n):
        cur = arr[i]
        # this loop effectively ensures a[i] = i+1 whenever it is possible.
        # The solution would be the first number in the list where this assignment
        # couldn't be made.
        while cur > 0 and cur <= n and arr[cur-1] != cur:
            # pythonic swap wasn't possible since the index is changed during swap
            tmp = arr[cur-1]
            arr[cur-1] = cur
            cur = tmp

    for i in range(n):
        if arr[i] != i+1:
            return i+1
    return n+1
####
print(lowest_skipped([3, 4, -1, 1]))
print(lowest_skipped([1, 2, 0]))
print(lowest_skipped([4, 3, 2, 1]))
