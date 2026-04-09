# Integer to Roman
# MEDIUM
# https://scaleengineer.com/dsa/problems/integer-to-roman

# Description
# Seven different symbols represent Roman numerals with the following values:
# Symbol 	Value
# I 	1
# V 	5
# X 	10
# L 	50
# C 	100
# D 	500
# M 	1000

# Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a 
# Roman numeral has the following rules:
# 1. If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to
#    the result, subtract its value, and convert the remainder to a Roman numeral.
#
# 2. If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol,
#    for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 
#    4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
#
# 3. Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D)
#    multiple times. If you need to append a symbol 4 times use the subtractive form.

# Given an integer, convert it to a Roman numeral.

# Example 1:
# Input: num = 3749
# Output: "MMMDCCXLIX"
# Explanation:
# 3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
#  700 = DCC as 500 (D) + 100 (C) + 100 (C)
#   40 = XL as 10 (X) less of 50 (L)
#    9 = IX as 1 (I) less of 10 (X)
# Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places

# Example 2:
# Input: num = 58
# Output: "LVIII"
# Explanation:
# 50 = L
#  8 = VIII

# Example 3:
# Input: num = 1994
# Output: "MCMXCIV"
# Explanation:
# 1000 = M
#  900 = CM
#   90 = XC
#    4 = IV

# Constraints:
#     1 <= num <= 3999

def IntToRomanGreedy(num):
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    result = []

    for i in range(len(values)):
        while values[i] <= num:
            result.append(symbols[i])
            num -= values[i]

    return "".join(result)

# Time: O(1)
# Space: O(1)
def IntToRomanLookup(num):
    thousands = ["", "M", "MM", "MMM"]
    hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    result = []
    
    result.append(thousands[num // 1000])
    num = num % 1000

    result.append(hundreds[num // 100])
    num = num % 100

    result.append(tens[num // 10])
    num = num % 10

    result.append(ones[num])

    return "".join(result)


def IntToRoman(num):
    return IntToRomanLookup(num)

if __name__ == "__main__":
    # Example 1:
    num = 3749
    expected = "MMMDCCXLIX"
    output = IntToRoman(num)
    print(num)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 2:
    num = 58
    expected = "LVIII"
    output = IntToRoman(num)
    print(num)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 3:
    num = 1994
    expected = "MCMXCIV"
    output = IntToRoman(num)
    print(num)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 4: Minimum value
    num = 1
    expected = "I"
    output = IntToRoman(num)
    print(num)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 5: Maximum value
    num = 3999
    expected = "MMMCMXCIX"
    output = IntToRoman(num)
    print(num)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 6: Simple case
    num = 10
    expected = "X"
    output = IntToRoman(num)
    print(num)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 7: Subtractive notation
    num = 4
    expected = "IV"
    output = IntToRoman(num)
    print(num)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 8: Hundreds
    num = 500
    expected = "D"
    output = IntToRoman(num)
    print(num)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 9: Mixed digits
    num = 1987
    expected = "MCMLXXXVII"
    output = IntToRoman(num)
    print(num)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 10: All digits
    num = 2468
    expected = "MMCDLXVIII"
    output = IntToRoman(num)
    print(num)
    print(expected)
    print(output)
    print(expected == output)
    print()
