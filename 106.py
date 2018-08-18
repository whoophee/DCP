# This problem was asked by Pinterest.
# Given an integer list where each number represents the number of hops you can
# make, determine whether you can reach to the last index starting at index 0.
# For example, [2, 0, 1, 0] returns true while [1, 1, 0, 1] returns false.
####
def traversible(hops):
    n = len(hops)
    cur_range = hops[0]
    for h in hops:
        if not cur_range:
            return False
        cur_range = max(cur_range - 1, h)
    return True
####
print(traversible([2, 0, 1, 0]))
print(traversible([1, 1, 0, 1]))
