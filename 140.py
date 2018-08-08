# This problem was asked by Facebook.
# Given an array of integers in which two elements appear exactly once and all
# other elements appear exactly twice, find the two elements that appear only once.
# For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8. The order does not matter.
# Follow-up: Can you do this in linear time and constant space?
####
# This is a generic functional programming feature.
def foldl(op, arr, initial):
    for a in arr:
        initial = op(initial, a)
    return initial

def non_repeating(arr):
    # Get an overall xor of the entire array. It gives x^y.
    xor = lambda x, y: x^y
    overall_xor = foldl(xor, arr, 0)

    # If a bit is set to 1, it implies that the corresponding bits of x and y
    # are different. The array can be partitioned using this.
    diff_bit = 1
    while not (diff_bit & overall_xor):
        diff_bit <<= 1

    # Although seperating arrays is a viable solution, it requires O(n) extra space.

    # The following function is defined to conditionally handle xoring with
    # either side of the partition based on the differential bit.
    def conditional_xor(prev, current):
        # if the bit is set, xor with the first element and return
        # if it is not, xor with the second element instead
        if diff_bit & current:
            return (prev[0]^current, prev[1])
        else:
            return (prev[0], prev[1]^current)

    return foldl(conditional_xor, arr, (0, 0))

print(non_repeating([3,3,4,4,16,32]))
