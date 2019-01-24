# This problem was asked by Walmart Labs.

# There are M people sitting in a row of N seats, where M < N. Your task is 
# to redistribute people such that there are no gaps between any of them, 
# while keeping overall movement to a minimum.

# For example, suppose you are faced with an input of [0, 1, 1, 0, 1, 0, 0, 0, 1], 
# where 0 represents an empty seat and 1 represents a person. In this case, one 
# solution would be to place the person on the right in the fourth seat. We can 
# consider the cost of a solution to be the sum of the absolute distance each 
# person must move, so that the cost here would be five.

# Given an input such as the one above, return the lowest possible cost of moving 
# people to remove all gaps.
####
def min_group_cost(arr):
    n = len(arr)
    cost_from_left = [0]*n
    cost_from_right = [0]*n

    num_ones = 0
    cur_cost = 0
    for i in range(n):
        if arr[i] == 0:
            cur_cost += num_ones
            cost_from_left[i] = cur_cost
        else:
            num_ones += 1
            cost_from_left[i] = cur_cost
    
    num_ones = 0
    cur_cost = 0
    for i in range(n-1, -1, -1):
        if arr[i] == 0:
            cur_cost += num_ones
            cost_from_right[i] = cur_cost
        else:
            num_ones += 1
            cost_from_right[i] = cur_cost
    
    return min([x+y for x, y in zip(cost_from_left, cost_from_right)])
####
print(min_group_cost([0, 1, 1, 0, 1, 0, 0, 0, 1]))



        





