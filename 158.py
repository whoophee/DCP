# This problem was asked by Slack.
# You are given an N by M matrix of 0s and 1s. Starting from the top left corner,
# how many ways are there to reach the bottom right corner?
# You can only move right and down. 0 represents an empty space while 1 represents a
# wall you cannot walk through.
# For example, given the following matrix:
# [[0, 0, 1],
#  [0, 0, 1],
#  [1, 0, 0]]
# Return two, as there are only two ways to get to the bottom right:
# •	Right, down, down, right
# •	Down, right, down, right
# The top left corner and bottom right corner will always be 0.
####
# simple DP problem
def num_paths(arr):
    m = len(arr)
    n = len(arr[0])
    num_paths = [[0]*n for _ in range(m)]
    num_paths[0][0] = 1

    # compute values for first column
    i = 1
    while i < m and arr[i][0] == 0:
        num_paths[i][0] = 1
        i += 1

    # compute values for first row
    i = 1
    while i < n and arr[0][i] == 0:
        num_paths[0][i] = 1
        i += 1

    # compute values for remaining
    for i in range(1, m):
        for j in range(1, n):
            num_paths[i][j] = num_paths[i-1][j] + num_paths[i][j-1]

    return num_paths[m-1][n-1]
####
mat = [[0, 0, 1], [0, 0, 0], [1, 0, 0]]
print(num_paths(mat))
