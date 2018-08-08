# Given an array consisting of n integers, find the contiguous subarray whose
# length is greater than or equal to k that has the maximum average value.
# And you need to output the maximum average value.
#
# Input: [1,12,-5,-6,50,3], k = 4
# Output: 12.75
# Explanation:
# when length is 5, maximum average value is 10.8,
# when length is 6, maximum average value is 9.16667.
# Thus return 12.75.
####
# BRUTE FORCE
def max_contiguous_subarray(arr, k):

    t = [0]
    n = len(arr)
    cur_sum = 0
    # calculate sum, it is used for later
    for a in arr:
        cur_sum += a
        t.append(cur_sum)

    cur_max = -10**7
    # iterate over available segment sizes
    for i in range(k, n+1):
        # iterate over all possible segments of that size
        for j in range(0, n-i+1):
            # calculate and reassign maximum average
            cur_avg = (t[j + i] - t[j])/i
            cur_max = max(cur_max, cur_avg)
    return cur_max
####
print(max_contiguous_subarray([1,12,-5,-6,50,3], 4))
