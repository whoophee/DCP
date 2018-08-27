# This problem was asked by Microsoft.
# Given a number in the form of a list of digits, return all possible permutations.
# For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].
####
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
permutes = {}
def _permute(cur):
    if cur == 1:
        return [[]]
    ret = []
    # iterate through possible options
    for i in range(10):
        # if divisible, the corresponding digit is addable
        if cur % primes[i] == 0:
            nxt = cur//primes[i]
            # if the combinations possible due to this number is not yet calculated
            if not permutes.get(nxt):
                permutes[nxt] = _permute(nxt)
            # extend the current list of permutations
            ret.extend([x + [i] for x in permutes[nxt]])
    return ret

def permutations(arr):
    prod = 1
    for x in arr:
        prod *= primes[x]
    return _permute(prod)
####
print(permutations([1, 2, 2, 3]))
