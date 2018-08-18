# This problem was asked by Google.
# Given two strings A and B, return whether or not A can be shifted some number of times to get B.
# For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.
####
def KMP_preprocess(arr):
    counter = 0
    ret = [0]
    for i in range(1, len(arr)):
        if arr[counter] == arr[i]:
            counter += 1
        else:
            counter = 0
        ret.append(counter)
    return ret
# double the second string and check if the first string is a substring of this.
def shifted(str1, str2):
    preprocessed = KMP_preprocess(str1)
    ctr = 0
    for c in str2 + str2:
        while c != str1[ctr] and ctr != 0:
            ctr = preprocessed[ctr - 1]
        if c == str1[ctr]:
            ctr += 1

        if ctr == len(str1):
            return True
    return False
####
print(shifted("abcde", "cdeab"))
print(shifted("abc", "acb"))
