# This problem was asked by Zillow.
# Let's define a "sevenish" number to be one which is either a power of 7, or 
# the sum of unique powers of 7. The first few sevenish numbers are 1, 7, 8, 49, 
# and so on. Create an algorithm to find the nth sevenish number.
####
def sevenish(n):
    # calculate binary representation of n
    # multiply corresponding powers of 7
    return int(bin(n)[2:], 7)
####
print(sevenish(5))