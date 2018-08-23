# This problem was asked by Microsoft.
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
# For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element sequence is [1, 2, 3, 4]. Return its length: 4.
####
def longest_seq(arr):
    arr_hashset = set(arr)
    ret = 0
    for x in arr:
        # beginning of a sequence
        if x-1 not in arr_hashset:
            ctr = 0
            cur = x
            # traverse entire sequence
            while cur in arr_hashset:
                cur += 1
                ctr += 1
                # update maximum
            ret = max(ctr, ret)
    return ret
####
print(longest_seq([100, 4, 200, 1, 3, 2]))
