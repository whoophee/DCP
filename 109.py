# This problem was asked by Cisco.
# Given an unsigned 8-bit integer, swap its even and odd bits. The 1st and 2nd bit
# should be swapped, the 3rd and 4th bit should be swapped, and so on.
# For example, 10101010 should be 01010101. 11100010 should be 11010001.
# Bonus: Can you do this in one line?
####
# If the number is x
# x & 10101010 gives even bits. Right shifting this brings these bits to odd indices.
# x & 1010101 gives odd bits. Left shifting this brings these bits to even indices.
# The solution is hence ((x & 10101010) >> 1) + ((x & 1010101) << 1)
def swap_bits(x):
    return ((x & 170)>>1) + ((x & 85)<<1)
####
t = int('11011001', 2)
print("{:b}".format(t))
swapped = swap_bits(t)
print("{:b}".format(swapped))
