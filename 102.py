# This problem was asked by Lyft.
# Given a list of integers and a number K, return which contiguous elements of the list sum to K.
# For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4].
####
# This solution appears more convoluted than it should be.

# Let us assume arr_sum is an array that maintains sum of values of arr from 0 to i
# This can be constructed in linear time and it would be strictly increasing (sorted).

# In this array, we have to find two indices such that the difference between them is
# exactly k (from the original problem)

# We initialize two counters 'begin' and 'end' both to 0.
# If arr_sum[end] - arr_sum[end] is greater than k, we would have to increase 'begin'
# Conversely, if the sum is less than k, we would increase 'end'
# If the difference is exactly k, we can return arr[begin : end+1] as the required solution

# Translating the new problem to our original problem, we do not have to maintain the entire
# array of sums, but just the current one
# In each iteration, add arr[i] to the current sum
# In each of these iterations, the beginning is moved up until the current sum is <= k
def sum_k(arr, k):
    s = 0
    beg = 0
    ret = []
    for i in range(len(arr)):
        s += arr[i]
        # Move 'begin' to a proper index
        while s > k:
            s -= arr[beg]
            beg += 1
        # Just compute all possible solutions
        if s == k:
            ret.append(arr[beg:i+1])
    return ret
####
print(sum_k([1, 2, 3, 4, 5], 9))
print(sum_k([1, 2, 3, 4, 5], 15))
print(sum_k([1, 2, 3, 4, 5], 12))
print(sum_k([3, 4, 5], 3))
