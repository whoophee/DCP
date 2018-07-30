# Leetcode 878
# A positive integer is magical if it is divisible by either A or B.
# Return the N-th magical number.  Since the answer may be very large, return it modulo 10^9 + 7.
# Example 1:
# Input: N = 1, A = 2, B = 3
# Output: 2
#
# Example 2:
# Input: N = 4, A = 2, B = 3
# Output: 6
#
# Example 3:
# Input: N = 5, A = 2, B = 4
# Output: 10
#
# Example 4:
# Input: N = 3, A = 6, B = 4
# Output: 8
####
from math import gcd

def lcm(a, b):
    return (a*b)/gcd(a, b)

def magical_number(n, A, B):
    LCM = lcm(A, B)
    below_lcm = LCM/A + LCM/B - 1

    lcm_counter = int(n/below_lcm)
    remain = n % below_lcm

    A_add = 0
    B_add = 0
    final_add = 0
    
    while remain:
        if A_add + A <= B_add + B:
            A_add += A
            final_add = A_add
        else:
            B_add += B
            final_add = B_add
        remain -= 1

    return int((lcm_counter * LCM) + final_add) % (10**9 + 7)
####
print(magical_number(1, 2, 3))
print(magical_number(4, 2, 3))
print(magical_number(5, 2, 4))
print(magical_number(2000, 7, 61))
