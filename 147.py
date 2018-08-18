# Given a list, sort it using this method: sorter(lst, i, j), which
# sorts lst from i to j.
####
# Arguably more efficient in C++, since the STL sort wouldn't require extra space.
def sorter(lst, i, j):
    return lst[:i] + sorted(lst[i:j]) + lst[j:]
####
print(sorter([1, 7, 5, 4, 3, 6], 2, 5))
