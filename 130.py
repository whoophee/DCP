# This problem was asked by Facebook.
# Given an array of numbers representing the stock prices of a company in chronological
#  order and an integer k, return the maximum profit you can make from k buys and sells.
#  You must buy the stock before you can sell it, and you must sell the stock before you can buy it again.
# For example, given k = 2 and the array [5, 2, 4, 0, 1], you should return 3.
####
def get_max_profit(arr, k):
    a = arr + [-1]
    current_min = a[0]
    current_max = a[0]
    ends = []
    # generate profit intervals
    # current_max == current_min denotes that the buying price was set during
    # the immediately previous loop (selling price not discovered yet)
    for i in range(1, len(a)):
        # more profit possible
        if a[i] > current_max:
            current_max = a[i]
        # the beginning of the next interval is found
        if a[i] < current_max and current_max != current_min:
            ends.append((current_min, current_max))
            current_max = a[i]
            current_min = a[i]
        # buying cost is strictly decreasing (to calculate cheapest buying price)
        if a[i] < current_min and current_max == current_min:
            current_min = a[i]
            current_max = a[i]

    # merge smallest intervals to make number of intervals = k
    while k < len(ends):
        # get smallest interval
        pos, cur = min(list(enumerate(ends)), key = lambda x: x[1][1] - x[1][0])
        # try merging with lower interval
        if pos != 0:
            lower = ends[pos-1]
            if cur[1] > lower[1]:
                ends[pos-1] = (lower[0], cur[1])
        # try merging with upper interval
        if pos != len(ends)-1:
            upper = ends[pos+1]
            if cur[0] < upper[0]:
                ends[pos+1] = (cur[0], upper[1])
        ends.remove(cur)

    return sum([y-x for x,y in ends])
####

print(get_max_profit([7, 9, 8, 11, 11, 10, 12, 15, 13, 10], 2))
