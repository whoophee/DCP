# This problem was asked by Google.
# Given a string of words delimited by spaces, reverse the words in string. For example,
# given "hello world here", return "here world hello"
# Follow-up: given a mutable string representation, can you perform this operation in-place?
####
def reverse_string(arr, i, j):
    n = j - i
    for x in range(int(n/2)):
        newx = n - x - 1
        arr[i + x], arr[i + newx] = arr[i + newx], arr[i + x]

def reverse_words(arr):
    start = 0
    n = len(arr)
    i = 0
    while i < n:
        # reverse each word individually
        if arr[i] == ' ':
            reverse_string(arr, start, i)
            start = i + 1
        i += 1
    # takes care of word terminated by end of array (instead of ' ')
    reverse_string(arr, start, i)
    # now reverse the entire string
    reverse_string(arr, 0, n)
####
t = list("1234 5678 ")
reverse_words(t)
print(t)
