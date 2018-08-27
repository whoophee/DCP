# Given two arrays A and B of equal size, the advantage of A with respect to B is
# the number of indices i for which A[i] > B[i].
# Return any permutation of A that maximizes its advantage with respect to B.
#
# Example 1:
# Input: A = [2,7,11,15], B = [1,10,4,11]
# Output: [2,11,7,15]
#
# Example 2:
# Input: A = [12,24,8,32], B = [13,25,32,11]
# Output: [24,32,8,12]
####
def argsort(arr):
    s = list(range(len(arr)))
    def get_val(i):
        return arr[i]
    return sorted(s, key = get_val)

def advantage_shuffle(a, b):
    a = sorted(a)
    b_argsort = argsort(b)
    n = len(a)
    ret = [0]*n
    j = 0
    last = n - 1

    for i in b_argsort:
        # Assign all numbers in A which are lower than currently evaluated number
        # in B to larger numbers in B. (since they can not be larger than any number)
        while j < n and last >= 0 and b[i] > a[j]:
            ret[b_argsort[last]] = a[j]
            j += 1
            last -= 1
        # all numbers in A are evaluated
        if j == n:
            break
        # Number greater than current B[i] is assigned to rightful index.
        ret[i] = a[j]
        j += 1

    return ret
####
print(advantage_shuffle([12,24,8,32], [13,25,32,11]))
