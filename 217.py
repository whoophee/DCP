# This problem was asked by Oracle.
# We say a number is sparse if there are no adjacent ones in its binary representation. 
# For example, 21 (10101) is sparse, but 22 (10110) is not. For a given input N, find the 
# smallest sparse number greater than or equal to N.
# Do this in faster than O(N log N) time.
####
def nearest_sparse(num):

    bin_digits = str(bin(num))[2:]

    n = len(bin_digits)
    i = 1
    most_recent_zeros = -1
    while i < n:
        if bin_digits[i] == bin_digits[i-1]:
            if bin_digits[i] == '0':
                most_recent_zeros = i
            else:
                break
        i += 1
    tmp = None
    if i == n:
        tmp = bin_digits
    elif most_recent_zeros == -1:
        tmp = '1' + '0'*n
    else:
        tmp = bin_digits[:most_recent_zeros] + '1' + '0' * (n-most_recent_zeros-1)

    return tmp, int(tmp, 2)


####
print(nearest_sparse(3))
print(nearest_sparse(19))
print(nearest_sparse(20))
print(nearest_sparse(int('10100110', 2)))
