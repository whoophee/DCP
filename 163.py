# This problem was asked by Jane Street.
# Given an arithmetic expression in Reverse Polish Notation, write a program to evaluate it.
# The expression is given as a list of numbers and operands. For example: [5, 3, '+'] should return 5 + 3 = 8.
# For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'] should return 5, since it is
# equivalent to ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.
# You can assume the given expression is always valid.
####
def rpolisheval(arr):
    st = []
    for x in arr:
        if x in ['+', '-', '*', '/']:
            n2 = st.pop()
            n1 = st.pop()
            st.append(eval('n1 {} n2'.format(x)))
        else:
            st.append(x)
    return st.pop()
####
print(rpolisheval([15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']))
