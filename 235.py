# This problem was asked by Facebook.
# Given an array of numbers of length N, find both the minimum and maximum using less than 2 * (N - 2) comparisons.
####
def min_max(arr, beg = None, end = None):
    if beg == None:
        beg = 0
        end = len(arr)
    if end - beg == 1:
        return arr[beg], arr[beg]
    if end - beg == 2:
        return min(arr[beg], arr[beg+1]), max(arr[beg], arr[beg+1])
    min1, max1 = min_max(arr, beg, (beg+end)//2)
    min2, max2 = min_max(arr, (beg+end)//2, end)
    return min(min1, min2), max(max1, max2)
####
print(min_max([1, 2, 3, 4, 5, 6, -2, 10, 11, -5, 7]))