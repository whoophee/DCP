# This problem was asked by Facebook.
# Given a positive integer n, find the smallest number of squared integers which sum to n.
# For example, given n = 13, return 2 since 13 = 32 + 22 = 9 + 4.
# Given n = 27, return 3 since 27 = 32 + 32 + 32 = 9 + 9 + 9.
####
# It is exactly the coin denomination problem. See solution to Problem #138 for details on the solution
class Coins:
    def get_coins(self, val):
        n = len(self.coins)
        # Minimum number of coins already calculated.
        if n > val:
            return self.coins[val]
        # iterate over uncalculated values
        for cur_val in range(n, val + 1):
            min_coins = None
            # iterate over denominations
            for denom in self.denominations:
                # ignore denomination if a valid solution is not possible out of it
                if cur_val - denom < 0 or self.coins[cur_val - denom] is None:
                    continue
                cur_coins = self.coins[cur_val - denom] + 1
                # Calculate minimum
                if not min_coins or cur_coins < min_coins:
                    min_coins = cur_coins

            self.coins.append(min_coins)
        return self.coins[val]

    def __init__(self, denominations = [1, 5, 10, 25]):
        self.denominations = sorted(denominations)
        min_denom = min(denominations)
        # the minimum denomination possible is assigned, since it is not possible
        # to get any lower values, they are assigned as None.
        self.coins = [0] + [None]*(min_denom - 1) + [1]
####
import math
def min_squares(x):
    denom = []
    for i in range(1, int(math.sqrt(x) + 1)):
        denom.append(i*i)
    t = Coins(denom)
    return t.get_coins(x)
####
print(min_squares(13))
print(min_squares(27))
print(min_squares(28))
