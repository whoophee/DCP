# This problem was asked by Google.
# You are given an array of length n + 1 whose elements belong to the set {1, 2, ..., n}.
# By the pigeonhole principle, there must be a duplicate. Find it in linear time and space.
####
def lul(arr):
    n = len(arr)
    return sum(arr) - (n*(n-1))//2
####
print(lul([1, 2, 3, 4, 3]))
