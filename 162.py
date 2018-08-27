# Good morning! Here's your coding interview problem for today.
# This problem was asked by Square.
# Given a list of words, return the shortest unique prefix of each word. For example, given the list:
# •	dog
# •	cat
# •	apple
# •	apricot
# •	fish
# Return the list:
# •	d
# •	c
# •	app
# •	apr
# •	f
####
def shortest_prefix(arr):
    letters = {chr(cur):{} for cur in range(ord('a'), ord('z')+1)}
    ret = []
    # generate a prefix counter for all the words.
    for word in arr:
        for i, c in enumerate(word):
            letters[c][i] = letters[c].get(i, 0) + 1
    # the point at which a character from a word appears to be unique,
    # can be assumed to be the unique prefix end point
    for word in arr:
        for i, c in enumerate(word):
            if letters[c][i] == 1:
                break
        # min to avoid exceeding word size if no unique prefix found
        ret.append(word[:min(i+1, len(word))])
    return ret
####
print(shortest_prefix(['dog', 'cat', 'apple', 'apricot', 'fish']))
