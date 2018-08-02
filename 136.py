# This question was asked by Google.
# Given an N by M matrix consisting only of 1's and 0's, find the largest rectangle containing only 1's and return its area.
# For example, given the following matrix:
# [[1, 0, 0, 0],
#  [1, 0, 1, 1],
#  [1, 0, 1, 1],
#  [0, 1, 0, 0]]
# Return 4.
####
# This portion of the problem deals with a seperate problem in itself
# https://www.geeksforgeeks.org/largest-rectangle-under-histogram/ is the problem in question
# The algorithm given however, is less than sufficient in explaining the solution
# For each bar in the histogram (index i and length arr[i])
# 1) If the stack is empty or if the length of the bar at the top of the stack
#    is lesser than the current bar, push i to the top of the stack.
# 2) If the length of the bar at the top of the stack is smaller, it means that
#    rectangles of all previously added bars (of greater length) end at this index.
#    a) If the bar at top of the stack (arr[stack[-1]]) is greater than the
#       currently considered bar, pop the bar and calculate its area as
#       arr[stack[-1]] * (i - stack[-1])
#    b) If the bar at the top of the stack is lesser, it means that the bar at index i
#       extends all the way to the index of the most recently removed bar of the stack.
#       Let the index of the most recently removed bar be x
#       Change arr[x] = arr[i] and push cur into the stack
# 3) If there are any remaining elements in the stack, do 2.a for the rest of the stack.
def maximum_rectangle_histogram(tmp):
    arr = tmp[:]
    stack = []
    current_maximum = 0
    for i in range(len(arr)):
        # add element to stack if stack is empty or if length of bar is greater than top of stack
        if not stack or arr[i] > arr[stack[-1]]:
            stack.append(i)
        else:
            cur = None
            # pop and calculate areas of all bars greater than the bar currently being considered
            while stack and arr[stack[-1]] >= arr[i]:
                cur = stack.pop()
                tmp = arr[cur]*(i - cur)
                if tmp > current_maximum:
                    current_maximum = tmp
            # update the index up to which the rectangle containing the current bar extends
            # add the index to the top of the stack as well
            if cur:
                arr[cur] = arr[i]
                stack.append(cur)
    # This part is unnecessary for the way max_rect() uses it. However, the generic
    # solution requires it.
    while stack:
        cur = stack.pop()
        tmp = arr[cur]*(i - cur)
        if tmp > current_maximum:
            current_maximum = tmp
    return current_maximum

def max_rect(arr):
    m = len(arr)
    n = len(arr[0])
    max_rect = 0
    sol = [[0]*(n+1) for _ in range(m + 1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            # DP over the length of bars for all indices
            if arr[i-1][j-1]:
                sol[i][j] = 1 + sol[i - 1][j]
        sol[i].append(0)
        # find maximum area using histogram of current row
        max_cur = maximum_rectangle_histogram(sol[i])
        if max_cur > max_rect:
            max_rect = max_cur
    return max_rect
####
arr = [[1, 0, 0, 0], [1, 0, 1, 1], [1, 0, 1, 1], [0, 1, 0, 0]]
print(max_rect(arr))
