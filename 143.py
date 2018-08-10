# This problem was asked by Amazon.
# Given a pivot x, and a list lst, partition the list into three parts.
# •	The first part contains all elemenets in lst that are less than x
# •	The second part contains all elemenets in lst that are equal to x
# •	The third part contains all elemenets in lst that are larger than x
# Ordering within a part can be arbitrary.
# For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], one partition may be [9, 3, 5, 10, 10, 12, 14]
####
# Using three individual lists and concatenating them seems like an obvious enough solution.
# This solution is aimed at performing this without using the O(n) extra space.

# swap numbers lower than x to their rightful place
def rightful_swap(arr, begin, end, x, lam):
    while True:
        # lam decides the objects that belong to the beginning portion of the array
        # assuming lam is a '<' operator, 'begin' increases until a value greater than
        # x is encountered (i.e. a value that doesn't belong in the first portion)
        while lam(arr[begin], x):
            begin += 1
        # conversely, this loop identifies an element that does not belong in the latter portion
        while not lam(arr[end], x):
            end -= 1
        # iterators have crossed each other
        if begin >= end:
            break
        # swappe elements
        arr[begin], arr[end] = arr[end], arr[begin]
    # this denotes the index at which the partition accurs
    return begin

def partitioned(arr, x):
    n = len(arr)
    # put all elements less than x in the correct part of the array
    new_begin = rightful_swap(arr, 0, n-1, x, lambda x, y: x < y)
    # the index at which the partition occurs, becomes the starting index of the
    # next partition
    # put all elements equal to x in the correct part of the array
    rightful_swap(arr, new_begin, n-1, x, lambda x, y: x == y)


####
t = [9, 12, 3, 5, 14, 10, 10]
partitioned(t, 10)
print(t)
