# This problem was asked by Google.
# Given a string which we can delete at most k, return whether you can make a palindrome.
# For example, given 'waterrfetawx' and a k of 2, you could delete f and x to get 'waterretaw'.
####

# This is presumably a DP problem where the number of characters to be deleted between arr[i] and arr[j] would be the subproblem.
# I chose to solve a much simpler problem in which, the longest palindromic subsequence is found. The length of this subsequence,
# subtracted from the overall length of the string would be the minimum number of characters to be removed to make it palindromic.
####
def palindrome_possible(s, k):
    n = len(s)
    # initialize DP array
    longest = [[0]*(n) for i in range(n)]
    for i in range(n):
        longest[i][i] = 1

    # length of substring currently considered
    for i in range(1, n):
        # end index of substring being considered
        for j in range(i, n):
            start = j - i
            end = j
            # basic lps subproblem statement
            if s[start] == s[end]:
                longest[start][end] = longest[start+1][end-1] + 2
            else:
                longest[start][end] = max(longest[start][end-1], longest[start+1][end])
    # longest subsequence must be possible to generate after deleting k characters
    return longest[0][n-1] > n - k
####
print(palindrome_possible('waterfetawx', 4))
