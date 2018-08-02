# This problem was asked by Facebook.
# Given a string and a set of delimiters, reverse the words in the string while
# maintaining the relative order of the delimiters. For example, given "hello/world:here", return "here/world:hello"
# Follow-up: Does your solution work for the following cases: "hello/world:here/",
# "hello//world:here"
####
import re
def reverse_words(input, delim):
    re_delimiter = '|'.join(delim)
    words = re.split(re_delimiter, input)
    seq_delims = re.findall(re_delimiter, input)
    words = words[::-1]
    final_string = words[0]
    for word, delim in zip(words[1:], seq_delims):
        final_string += delim + word
    return final_string
####
print(reverse_words("hello//world:here", ['/',':']))
print(reverse_words("hello/world:here/", ['/',':']))
