# This problem was asked by Triplebyte.
# You are given n numbers as well as n probabilities that sum up to 1.
# Write a function to generate one of the numbers with its corresponding probability.
# For example, given the numbers [1, 2, 3, 4] and probabilities [0.1, 0.5, 0.2, 0.2],
# your function should return 1 10% of the time, 2 50% of the time, and 3 and 4 20%
# of the time.
# You can generate random numbers between 0 and 1 uniformly.
####
import random
class RandVal:
    def get_rand(self):
        tmp = random.random()
        for i in range(self.n):
            if tmp < self.prob[i]:
                self.counts[i] += 1
                return self.arr[i]

    def descr(self):
        s = sum(self.counts)
        return [x/s for x in self.counts]

    def __init__(self, arr = [1, 2, 3, 4], prob = [0.1, 0.5, 0.2, 0.2]):
        self.arr = arr
        self.n = len(arr)
        self.counts = [0]*len(arr)

        s = 0
        self.prob = []
        for x in prob:
            s += x
            self.prob.append(s)
####
r = RandVal()
for _ in range(10**5):
    r.get_rand()
print(r.descr())
