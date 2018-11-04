# This problem was asked by Goldman Sachs.
# You are given N identical eggs and access to a building with k floors. 
# Your task is to find the lowest floor that will cause an egg to break, 
# if dropped from that floor. Once an egg breaks, it cannot be dropped 
# again. If an egg breaks when dropped from the xth floor, you can assume 
# it will also break when dropped from any floor greater than x.
# Write an algorithm that finds the minimum number of trial drops it will 
# take, in the worst case, to identify this floor.
# For example, if N = 1 and k = 5, we will need to try dropping the egg 
# at every floor, beginning with the first, until we reach the fifth floor, 
# so our solution will be 5.
####
def min_eggs(n, k):
    steps = [[0]*(k+1) for _ in range(n+1)]
    # defaults for 0 or 1 floors
    for i in range(n+1):
        steps[i][0] = 0
        steps[i][1] = 1
    # defualt for 1 egg
    for i in range(k+1):
        steps[1][i] = i

    for num_eggs in range(2, n+1):
        for num_floors in range(2, k+1):
            n_steps = []
            # The egg can either break, or stay intact
            ## if it breaks, num_steps = 1 + steps[num_eggs-1][cur_floors-1] (only floors beneath)
            ## if it doesn't, num_steps = 1 + steps[num_eggs][total_floors - cur_floors] (only floors above)
            # Maximum possible at any floor is considered.
            # The intermediate floor is chosen such that this is minimized
            for x in range(1, num_floors+1):
                tmp = 1 + max(steps[num_eggs-1][x-1], steps[num_eggs][num_floors-x])
                n_steps.append(tmp)
            steps[num_eggs][num_floors] = min(n_steps)

    return steps[n][k]
####
print(min_eggs(2, 100))