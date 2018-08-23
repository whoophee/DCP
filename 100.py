# This problem was asked by Google.
# You are in an infinite 2D grid where you can move in any of the 8 directions:
#  (x,y) to
#     (x+1, y),
#     (x - 1, y),
#     (x, y+1),
#     (x, y-1),
#     (x-1, y-1),
#     (x+1,y+1),
#     (x-1,y+1),
#     (x+1,y-1)
# You are given a sequence of points and the order in which you need to cover the points.
# Give the minimum number of steps in which you can achieve it. You start from the first point.
# Example:
# Input: [(0, 0), (1, 1), (1, 2)]
# Output: 2
# It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).
####
def moves(arr):
    dist = 0
    for i in range(1, len(arr)):
        x1, y1 = arr[i]
        x2, y2 = arr[i-1]
        dist += max(abs(x1 - x2), abs(y1 - y2))
    return dist
####
print(moves([(0, 0), (1, 1), (1, 2)]))
