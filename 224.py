# This problem was asked by Amazon.
# Given a sorted array, find the smallest positive integer that is not the sum of a subset of the array.
# For example, for the input [1, 2, 3, 10], you should return 7.
# Do this in O(N) time.
####
def smallest_not_possible(in_list):
    cur_poss = 1
    for x in in_list:
        # if the current element is less than previous possible sum, it is still reachable
        if x <= cur_poss:
            cur_poss += x
        # there is a disconnect
        else:
            break
    return cur_poss
####
print(smallest_not_possible([1, 2, 3, 10]))