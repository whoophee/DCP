# This problem was asked by Palantir.
# Given a number represented by a list of digits, find the next greater permutation of a
# number, in terms of lexicographic ordering. If there is not greater permutation possible,
# return the permutation with the lowest value/ordering.
# For example, the list [1,2,3] should return [1,3,2]. The list [1,3,2] should return [2,1,3].
# The list [3,2,1] should return [1,2,3].
# Can you perform the operation without allocating extra memory (disregarding the input memory)?
####
def next_perm(arr):
    n = len(arr)
    i = n-1
    while i > 0:
        arr[i], arr[i-1] = arr[i-1], arr[i]
        if arr[i-1] > arr[i]:
            return arr
        i -= 1
    return sorted(arr)
####
print(next_perm([1, 4, 3, 2]))
