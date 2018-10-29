# This problem was asked by Square.
# In front of you is a row of N coins, with values v1, v1, ..., vn.
# You are asked to play the following game. You and an opponent take turns 
# choosing either the first or last coin from the row, removing it from the 
# row, and receiving the value of the coin.
# Write a program that returns the maximum amount of money you can win with 
# certainty, if you move first, assuming your opponent plays optimally.
####
def best_possible(coins):
    n = len(coins)
    a = [[(0, 0)]*n for _ in range(n)]

    for i in range(n):
        a[i][i] = (coins[i], 0)
    for i in range(n-1):
        c1, c2 = coins[i], coins[i+1]
        a[i][i+1] = (max(c1, c2), min(c1, c2))
    
    for gap_size in range(2, n):
        for begin in range(0, n - gap_size):
            end = begin + gap_size
            # if player chooses coin from the beginning
            choose_begin = coins[begin] + a[begin+1][end][1]
            # if player chooses coin from the end
            choose_end = coins[end] + a[begin][end-1][1]
            # p1 => score of 1st player
            # p2 => score of 2nd player
            p1, p2 = None, None
            if choose_begin < choose_end:
                p1 = choose_end
                p2 = a[begin][end-1][0]
            else:
                p1 = choose_begin
                p2 = a[begin+1][end][0]
            a[begin][end] = (p1, p2)
    return a[0][n-1]
####
print(best_possible([5, 3, 7, 10]))
print(best_possible([8, 15, 3, 7]))



####