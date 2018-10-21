# This problem was asked by Facebook.
# Given a number in Roman numeral format, convert it to decimal.
# The values of Roman numerals are as follows:
# {
#     'M': 1000,
#     'D': 500,
#     'C': 100,
#     'L': 50,
#     'X': 10,
#     'V': 5,
#     'I': 1
# }
# In addition, note that the Roman numeral system uses subtractive notation for numbers such as IV and XL.
# For the input XIV, for instance, you should return 14.
####
class RomanInt:
    def __init__(self):
        units = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        thousands = ['', 'M', 'MM', 'MMM']
        stored = {}

        for i in range(1, 4000):
            cur = ''
            cur += thousands[i//1000]
            cur += hundreds[(i%1000)//100]
            cur += tens[(i%100)//10]
            cur += units[i%10]
            stored[cur] = i
        self.roman_to_int = stored
####
ri = RomanInt()
print(ri.roman_to_int['MMMCMXCIX'])
