# This problem was asked by Yahoo.
# Write a function that returns the bitwise AND of all integers between M and N, inclusive.
####
def range_and(M, N):
    lsb = lambda x: x & -x

    
    if N <= M + 1:
        return N & M
    
    cur = 1 if M == 0 else M

    while cur + lsb(cur) <= N:
        cur += lsb(cur)
    
    return cur
####
print(range_and(4, 7))