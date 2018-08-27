# This problem was asked by Google.
# Given a string, return the first recurring character in it, or null if there is no recurring chracter.
# For example, given the string "acbbac", return "b". Given the string "abcdef", return null.
####
def first_repeat(s):
    tmp = {}
    for x in s:
        if tmp.get(x):
            return x
        tmp[x] = True
    return None
####
print(first_repeat("acbbac"))
print(first_repeat("abcdef"))
