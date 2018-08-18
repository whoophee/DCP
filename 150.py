# This problem was asked by LinkedIn.
# Given a list of points, a central point, and an integer k, find the nearest k
# points from the central point.
# For example, given the list of points [(0, 0), (5, 4), (3, 1)], the central point
# (1, 2), and k = 2, return [(0, 0), (3, 1)].
####
from heapq import heappush, heappushpop
def nearest_k(points, centre, k):
    # This is a min-heap
    min_hp = []
    n = len(points)
    ret = []
    # squared distance
    dist = lambda x, y: (x[0] - y[0])**2 + (x[1] - y[1])**2

    # iterate over all available points
    for i in range(n):
        p = points[i]
        cur_dist = dist(p, centre)
        # first n-k points are inserted into the minheap with distance to centre
        # as their priority
        if i < n-k:
            heappush(min_hp, (cur_dist, p))
        # the remaining k points are inserted using a pushpop operation, which
        # causes the pop of k minimums.
        else:
            tmp = heappushpop(min_hp, (cur_dist, p))
            ret.append(tmp[1])
    return ret
####
print(nearest_k([(0, 0), (5, 4), (3, 1)], (1, 2), 2))
