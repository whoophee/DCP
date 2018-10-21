# This problem was asked by Dropbox.
# Spreadsheets often use this alphabetical encoding for its columns: "A", "B",
# "C", ..., "AA", "AB", ..., "ZZ", "AAA", "AAB", ....
# Given a column number, return its alphabetical column id. For example, given 1,
# return "A". Given 27, return "AA".
####
def int_base26(val):
    baseval = ord('A') - 1
    ret = ''
    cur = val
    while cur:
        ret = chr(baseval + cur % 26) + ret
        cur //= 26
    return ret
####
print(int_base26(27))
print(int_base26(57))
