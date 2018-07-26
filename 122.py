# This question was asked by Zillow.
# You are given a 2-d matrix where each cell represents number of coins in that cell. Assuming we start at matrix[0][0], and can only move right or down, find the maximum number of coins you can collect by the bottom right corner.
# For example, in this matrix
# 0 3 1 1
# 2 1 0 4
# 1 5 3 1
# The most we can collect is 0 + 3 + 1 + 5 + 3 + 1 = 13 coins.
####
# This is a pretty straightforward DP problem. No antics.
# Let coin[m][n] be the input matrix
# The i, j index of the grid could be reached from i-1, j or i, j-1
# reward[i][j] = max(reward[i-1][j], reward[i][j-1]) + coin[i][j]
####
def max_coins(coins):

    m = len(coins)
    n = len(coins[0])

    reward = [[0]*n for i in range(m)]

    reward[0][0] = coins[0][0]

    for i in range(1, m):
        reward[i][0] = reward[i-1][0] + coins[i][0]

    for i in range(1, n):
        reward[0][i] = reward[0][i-1] + coins[0][i]

    for i in range(1, m):
        for j in range(1, n):
            reward[i][j] = max(reward[i][j-1], reward[i-1][j]) + coins[i][j]

    return reward[m-1][n-1]


####
inputarr = [[0, 3, 1, 1], [2, 1, 0, 4], [1, 5, 3, 1]]

print(max_coins(inputarr))
