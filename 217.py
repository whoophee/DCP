# This problem was asked by Oracle.
# We say a number is sparse if there are no adjacent ones in its binary representation. 
# For example, 21 (10101) is sparse, but 22 (10110) is not. For a given input N, find the 
# smallest sparse number greater than or equal to N.
# Do this in faster than O(N log N) time.
####
def nearest_sparse(num):
    # get the binary representation of the integer
    bin_digits = str(bin(num))[2:]

    n = len(bin_digits)
    i = 1
    most_recent_zeros = -1

    # Find the most recent instance of continuous zeros. It is used later.
    # If there exists continuous '1's, it is not sparse and must be modified.
    while i < n:
        if bin_digits[i] == bin_digits[i-1]:
            if bin_digits[i] == '0':
                most_recent_zeros = i
            else:
                break
        i += 1
    tmp = None
    # If the original number is sparse, return the number as is
    if i == n:
        tmp = bin_digits
    # if the number is not sparse, we find the first instance at which a modification is required.
    # e.g. 
    # Consider 1011XXXX. 
    # Here, an immediately larger number must be found to remove the current unsparseness.
    # This string would thus become 11000000. However this is still not sparse.
    # This would then become 100000000.
    # From inspection, we can see that this would always happen in the absence of continuous zeroes.
    # This repeated unsparsing would stop at the closest occurence of repeated zeroes.

    # Thus, for any string 
    # XXXX 00 YYY 11 ZZZZZ, the closest sparse number would be 
    # XXXX 01 000 00 00000
    else:
        tmp = bin_digits[:most_recent_zeros] if most_recent_zeros != -1 else ''
        tmp += '1' + '0' * (n-most_recent_zeros-1)    
    
    return tmp, int(tmp, 2)


####
print(nearest_sparse(3))
print(nearest_sparse(19))
print(nearest_sparse(20))
print(nearest_sparse(int('10100110', 2)))
