# This problem was asked by Google.
# Given a set of closed intervals, find the smallest set of numbers that covers all the intervals.
# If there are multiple smallest sets, return any of them.
# For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9], one set of numbers
# that covers all these intervals is {3, 6}.
####
def cover(intervals):
    # sort by end of interval
    intervals = sorted(intervals, key = lambda x:x[1])
    begin = intervals[0][1]
    ret = [begin]

    for i in intervals:
        if i[0] <= begin:
            continue
        ret.append(i[1])
        begin = i[1]
    return ret
####
print(cover([[0, 3], [2, 6], [3, 4], [6, 9]]))
