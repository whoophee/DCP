# This question was asked by Google.
# Given an integer n and a list of integers l, write a function that randomly
# generates a number from 0 to n-1 that isn't in l (uniform).
####
import random

class CustomRandom:
    def rand(self):
        tmp = random.randint(0, self.k)
        # return as is if there's no mapping for the generated number
        return self.alt_map.get(tmp, tmp)

    def __init__(self, n, l):
        k = n - len(l)
        # WOuld otherwise require O(n) operations in the future
        l = set(l)
        alts = {}
        ctr = n-1
        # The idea is, a random number is generated from 0 to k where k = n - len(l)
        # Any number that shouldn't be returned is mapped to an allowed number beyond k
        for x in l:
            if x < k:
                while ctr in l:
                    ctr -= 1
                alts[x] = ctr
        self.alt_map = alts
        self.k = k
####
c = CustomRandom(10, [2, 3, 8, 9])
hm = {}
for _ in range(10000):
    cur = c.rand()
    hm[cur] = hm.get(cur, 0) + 1
print(hm)
