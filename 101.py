# This problem was asked by Alibaba.
# Given an even number (greater than 2), return two prime numbers whose sum will be equal to the given number.
# A solution will always exist. See https://en.wikipedia.org/wiki/Goldbach%27s_conjecture.
# Example:
# Input: 4
# Output: 2 + 2 = 4
# If there are more than one solution possible, return the lexicographically smaller solution.
# If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, then
# [a, b] < [c, d]
# If a < c OR a==c AND b < d.
####
def primes(x):
    sieve = [True]*x
    sieve[0] = sieve[1] = False
    i = 2
    while i*i < x:
        if sieve[i]:
            for cur in range(i*i, x, i):
                sieve[cur] = False
        i += 1
    return [i for i, x in enumerate(sieve) if x]


def goldbach_pair(x):
    p = primes(x)
    beg = 0
    end = len(p)-1
    while beg < end:
        cur = p[beg] + p[end]
        if cur > x:
            end -= 1
        elif cur < x:
            beg += 1
        else:
            return p[beg], p[end]
####
print(goldbach_pair(10))
