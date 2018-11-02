# This problem was asked by Twitter.
# Given a list of numbers, create an algorithm that arranges them in 
# order to form the largest possible integer. For example, given 
# [10, 7, 76, 415], you should return 77641510.
####
def largest_possible(numlist):
    strlist = [str(num) for num in numlist]
    maxlen = len(max(strlist, key=lambda x: len(x)))
    # Key is used because using comparator functions isn't good Pythonic practice.
    # This function repeats the last character to maximum length
    # eg:   7 becomes 777
    #       76 becomes 766
    # This gives a method to ascertain the effective priority of one number over another
    def transform(x):
        return x + (maxlen - len(x))*x[-1]
    return sorted(strlist, key = transform, reverse = True)
####
print(largest_possible([10, 7, 76, 415]))