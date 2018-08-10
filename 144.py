# This problem was asked by Google.
# Given an array of numbers and an index i, return the index of the nearest larger
# number of the number at index i, where distance is measured in array indices.
# For example, given [4, 1, 3, 5, 6] and index 0, you should return 3.
# If two distances to larger numbers are the equal, then return any one of them.
# If the array at i doesn't have a nearest larger integer, then return null.
# Follow-up: If you can preprocess the array, can you do this in constant time?
####
# There is reusable code that can be refactored into a single function. It is
# maintained as is, for readability.
def nearest_preprocess(arr):
    n = len(arr)
    # tmp is a stack
    tmp = []
    sol = [None]*n

    # Traverse the array in forward direction
    for i in range(n):
        # As long as the stack is non-empty and the value corresponding to the
        # top of the stack is less than the value of currently being considered,
        # pop the top of the stack and assign i as the index, whose element is
        # nearest to and greater than the element at the popped index.
        while tmp and arr[i] > arr[tmp[-1]]:
            cur = tmp.pop()
            sol[cur] = i
        # Add current index to stack
        tmp.append(i)
    tmp = []

    # Perform the above described process in reverse to discover the nearest
    # bigger value behind the current index. Replace precalculated index if the new
    # distance is lesser.
    for i in range(n-1, -1, -1):
        while tmp and arr[i] > arr[tmp[-1]]:
            cur = tmp.pop()
            # Compare with previous distance
            if not sol[cur] or cur - i < i - sol[cur]:
                sol[cur] = i
        tmp.append(i)

    return sol
####
print(nearest_preprocess([4, 1, 3, 5, 6]))
