# This problem was asked by Google.
# Find the minimum number of coins required to make n cents.
# You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.
# For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.
####
# A very basic DP problem
# Iterate over all uncalculated values in axcending order
# For each of these values (val)
#   Iterate over all available denominations
#   For each of these denominations, check if coins(val - denom) is a valid solution
#   Thus, coins(val) = min(coins(val - denom)) for all available denom
# The loop can be broken once the required value is reached

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
c = Coins()
print(c.get_coins(5))
print(c.get_coins(16))
print(c.coins)
