# This problem was asked by Facebook.
# Given a 32-bit integer, return the number with its bits reversed.
# For example, given the binary number 1111 0000 1111 0000 1111 0000 1111 0000,
# return 0000 1111 0000 1111 0000 1111 0000 1111.
####
def reverse32(x):
    ret = 0
    for _ in range(32):
        ret = (ret<<1) + (x&1)
        x >>= 1
    return ret
####
t = int('10110000111100001111000011110001', 2)
print("{:b}".format(t))
print("{:b}".format(reverse32(t)))
