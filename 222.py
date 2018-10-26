# This problem was asked by Quora.
# Given an absolute pathname that may have . or .. as part of it, return the shortest standardized path.
# For example, given "/usr/bin/../bin/./scripts/../", return "/usr/bin/".
####
def relative_path(cur_path):
    st = []
    for c in cur_path.split('/'):
        if c == '.':
            pass
        elif c == '..':
            st.pop()
        else:
            st.append(c)
    return '/'.join(st)
####
print(relative_path("/usr/bin/../bin/./scripts/../"))