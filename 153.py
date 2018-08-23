# Find an efficient algorithm to find the smallest distance (measured in number of words)
# between any two given words in a string.
# For example, given words "hello", and "world" and a text content of
# "dog cat hello cat dog dog hello cat world", return 1 because there's only one
# word "cat" in between the two words.
####
def min_dist(words, w1, w2):
    words = words.split(" ")
    start = None
    ret = len(words)
    for i, w in enumerate(words):
        if w == w1:
            start = i
        if w == w2 and start:
            ret = min(ret, i-start-1)
            start = None
    return ret
####
print(min_dist("dog cat hello cat dog dog hello cat world", "hello", "world"))
