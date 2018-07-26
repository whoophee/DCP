# This problem was asked by Google.
# Given a sorted list of integers, square the elements and give the output in sorted order.
# For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
####
def squared_sorted(arr):
    begin = 0
    end = len(arr) - 1
    ret = []
    while begin <= end:
        if arr[begin]**2 > arr[end]**2:
            ret.append(arr[begin]**2)
            begin += 1
        else:
            ret.append(arr[end]**2)
            end -= 1
    return ret[::-1]
####
print(squared_sorted([-9, -2, 0, 2, 3]))
