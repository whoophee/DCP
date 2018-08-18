# This problem was asked by Square.
# Given a string and a set of characters, return the shortest substring containing
# all the characters in the set. For example, given the string "figehaeci" and the
# set of characters {a, e, i}, you should return "aeci". If there is no substring
# containing all the characters in the set, return null.
####
def char_prime(ch):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    return primes[ord(ch) - ord('a')]

def anagram_hash(s):
    ret = 1
    for ch in s:
        ret *= char_prime(ch)
    return ret

def substring_contains(s, chars):
    t = anagram_hash(chars)
    min_len = len(chars)
    n = len(s)

    # iterate over all possible lengths
    for i in range(min_len, n+1):
        # generate product of first i-1 characters
        cur_hash = anagram_hash(s[:i-1])
        # iterate over all strings of i length
        for j in range(n - i + 1):
            # calculate current product
            cur_hash *= char_prime(s[j+i-1])
            # if product is divisible by required character product it is a solution
            if cur_hash % t == 0:
                return s[j:j+i]
            cur_hash /= char_prime(s[j])
    # this point is reached if no solution was obtained previously
    return None
####
print(substring_contains('figahaeci', ['a', 'i']))
