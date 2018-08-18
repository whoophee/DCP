# Given a list of numbers, return whether any two sums to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?
####
def sum_exists(arr, k):
    t = set()
    for a in arr:
        t.add(a)
        if k-a in t:
            return True
    return False
####
print(sum_exists([10, 15, 3, 7]))
