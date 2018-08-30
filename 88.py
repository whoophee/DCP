# This question was asked by ContextLogic.
# Implement division of two positive integers without using the division,
# multiplication, or modulus operators. Return the quotient as an integer, ignoring the remainder.
####
def weird_divide(a, b):
    # find the largest power of two above the given number
    ctr = 0
    while (b << ctr) < a:
        ctr += 1
    ctr -= 1
    cur_sum = 0
    cur_div = 0
    # extract binary digits of the quotient
    while ctr >= 0:
        # accomodate an extra bit in the quotient
        cur_div <<= 1
        # multiply with current power of two
        new_sum = (b << ctr) + cur_sum
        ctr -= 1
        # the recently added power of 2 is valid
        if new_sum < a:
            cur_sum = new_sum
            cur_div += 1
            
    return cur_div
####
print(weird_divide(103, 2))
