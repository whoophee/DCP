# This problem was asked by Amazon.
# Given a string, determine whether any permutation of it is a palindrome.
# For example, carrace should return true, since it can be rearranged to form racecar,
# which is a palindrome. daily should return false, since there's no rearrangement that can form a palindrome.
####
def anagram_palindrome(s):
    bits = [1<<x for x in range(26)]
    p = 0
    n = len(s)
    # xor all the elements
    for ch in s:
        p ^= bits[ord(ch) - ord('a')]
    # palindrome is possible if the xor folds to 0
    # if it doesn't, we also check if it has odd number of letters and a single unpaired letter
    return (p == 0) or (n % 2 and p in bits)
####
print(anagram_palindrome('carrace'))
print(anagram_palindrome('daily'))
