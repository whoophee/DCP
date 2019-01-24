# This problem was asked by Quantcast.
# You are presented with an array representing a Boolean expression. 
# The elements are of two kinds:
# •	T and F, representing the values True and False.
# •	&, |, and ^, representing the bitwise operators for AND, OR, and XOR.
# Determine the number of ways to group the array elements using parentheses 
# so that the entire expression evaluates to True.
# For example, suppose the input is ['F', '|', 'T', '&', 'T']. In this case, 
# there are two acceptable groupings: (F | T) & T and F | (T & T).
####
# This is horrible, but works in O(n^3) time and O(n^2) space
def get_sol(arr):
    
    op = {
        '|': lambda x, y: x | y,
        '&': lambda x, y: x & y,
        '^': lambda x, y: x ^ y
    }

    n = len(arr)

    dp = {False: {}, True: {}}

    for i in range(0, n, 2):
        if arr[i] == 'T':
            dp[True][(i, i)] = 'T'
        else:
            dp[False][(i, i)] = 'F'

    for k in range(2, n, 2):
        for i in range(0, n - k, 2):
            begin = i
            end = i + k
            for j in range(begin, end, 2):
                left = (begin, j) 
                right = (j + 2, end)
                cur_op = op[arr[j + 1]]
                for x, y in [(True, True), (True, False), (False, True), (False, False)]:
                    if (left in dp[x]) and (right in dp[y]):
                        dp[cur_op(x, y)][(begin, end)] = '({}{}{})'.format(dp[x][left], arr[j+1], dp[y][right])

    return dp.get(True, {}).get((0, n-1))
####
print(get_sol(['F', '|', 'T', '&', 'T']))
                


                





