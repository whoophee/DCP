# This problem was asked by Google.
# Given a word W and a string S, find all starting indices in S which are anagrams of W.
# For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.
####
# assume every letter is in lowercase
def char_prime(ch):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    return primes[ord(ch) - ord('a')]

def anagram_hash(s):
    ret = 1
    for ch in s:
        ret *= char_prime(ch)
    return ret

def anagram_indices(W, S):
    wval = anagram_hash(W)
    n = len(W)
    cur = anagram_hash(S[:n-1])
    ret = []
    for i in range(len(S) - n + 1):
        cur *= char_prime(S[i+n-1])
        if wval == cur:
            ret.append(i)
        cur /= char_prime(S[i])
    return ret
####
print(anagram_indices("ab", "abxaba"))
