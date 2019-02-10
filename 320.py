# This problem was asked by Amazon.
# Given a string, find the length of the smallest window that 
# contains every distinct character. Characters may appear more 
# than once in the window.
#
# For example, given "jiujitsu", you should return 5, corresponding 
# to the final five letters.
####
def smallest_window(inp):
    reqd = len(set(inp))

    n = len(inp)

    begin = 0
    end = 0
    counts = {}

    best = n

    # iterate the end of the window
    while end < n:
        # increment the count of the letter
        if not inp[end] in counts:
            counts[inp[end]] = 0
        counts[inp[end]] += 1
        end += 1

        # now shrink the beginning of the window as long as required
        # characters are still present within the window
        while len(counts) == reqd and counts[inp[begin]] > 1:
            counts[inp[begin]] -= 1
            begin += 1
        
        # reassign the minimum window
        if len(counts) == reqd:
            best = min(best, end - begin)
    
    return best
####
print(smallest_window("jiujitsu"))

        




