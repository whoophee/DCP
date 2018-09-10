# This problem was asked by Facebook.
# Given an N by N matrix, rotate it by 90 degrees clockwise.
# For example, given the following matrix:
# [[1, 2, 3, 4],
#  [5, 6, 7, 8],
#  [9, 10, 11, 12],
#  [13, 14, 15, 16]]
# you should return:
# Follow-up: What if you couldn't use any extra space?
####
def rotate90(arr):
    n = len(arr)
    begin = 0
    end = n-1
    while begin < end:
        for i in range(begin, end):
            x0, y0 = begin, i
            x1, y1 = i, end
            x2, y2 = end, n-1 - i
            x3, y3 = n-1-i, begin
            arr[x0][y0], arr[x1][y1], arr[x2][y2], arr[x3][y3] = arr[x3][y3], arr[x0][y0], arr[x1][y1], arr[x2][y2]
        begin += 1
        end -= 1

def matrix_print(arr):
    print('\n'.join(['\t'.join([str(x) for x in y]) for y in arr]))
####
t = [[1, 2, 3, 4],
 [5, 6, 7, 8],
 [9, 10, 11, 12],
 [13, 14, 15, 16]]
matrix_print(t)
print()
rotate90(t)
matrix_print(t)
