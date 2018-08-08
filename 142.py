# This problem was asked by Google.
# You're given a string consisting solely of (, ), and *. * can represent either a
#  '(', ')', or an empty string. Determine whether the parentheses are balanced.
# For example, (()* and (*) are balanced. )*( is not balanced.
####
# Two variables l (low) and h (high) are used to maintain how balanced the string is.
# The evaluation is as follows:
# 1.) If the character currently being evaluated is an '(', the minimum indentation
#     possible, increases. If it is a '*' or a ')', the lowest possible indentation
#     decreses.
# 2.) Conversely, if the character is ')', the highest possible indentation decreases.
#     It increases if the character is a '(' or a '*'.

def valid_string(arr):
    l = h = 0

    for s in arr:
        # Lowest possible indentation evaluated
        l += 1 if s == '(' else -1
        l = max(l, 0)
        # Highest possible indentation evaluated
        h += -1 if s == ')' else 1
        # If highest possible indentation is less than 0, it implies an excessive
        # number of ')' that '*' has not been able to balance out.
        if h < 0:
            return False
    # A low that is greater than zero, implies excessive '(' that wasn't balanced.
    return l == 0
####
print(valid_string("(()*"))
print(valid_string(")*("))
