# Given a list of elements, find the majority element, which appears more than
# half the times (> floor(len(lst) / 2.0)).
# You can assume that such element exists.
# For example, given [1, 2, 1, 1, 3, 4, 1], return 1.
####
def majority(arr):
    ctr = 0
    maj = None
    for x in arr:
        if ctr == 0:
            maj = x
        ctr += 1 if maj == x else -1
    return maj
####
print(majority([1, 2, 1, 1, 3, 4, 1]))
