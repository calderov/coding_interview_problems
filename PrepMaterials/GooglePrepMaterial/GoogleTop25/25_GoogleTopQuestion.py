# Valid Number
# HARD
# https://scaleengineer.com/dsa/problems/valid-number

# Description
# Given a string s, return whether s is a valid number.
# For example, all the following are valid numbers: 
#   "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"

# while the following are not valid numbers:
#   "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53".

# Formally, a valid number is defined using one of the following definitions:
#     An integer number followed by an optional exponent.
#     A decimal number followed by an optional exponent.

# An integer number is defined with an optional sign '-' or '+' followed by digits.

# A decimal number is defined with an optional sign '-' or '+' followed by one of the following definitions:
#     Digits followed by a dot '.'.
#     Digits followed by a dot '.' followed by digits.
#     A dot '.' followed by digits.

# An exponent is defined with an exponent notation 'e' or 'E' followed by an integer number.

# The digits are defined as one or more digits.
 
# Example 1:
# Input: s = "0"
# Output: True

# Example 2:
# Input: s = "e"
# Output: False

# Example 3:
# Input: s = "."
# Output: False

# Constraints:
#   1 <= s.length <= 20
#    s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.

# Time: O(n)
# Space: O(1)
def ValidNumber(s):
    if not s:
        return False

    digits = "0123456789"
    hasDigits = False
    hasDecimal = False
    hasExponential = False

    for i in range(len(s)):
        c = s[i].lower()

        if c in digits:
            hasDigits = True
            continue

        if c == ".":
            if hasDecimal:
                return False
            hasDecimal = True
            continue

        if c == "-" or c == "+":
            if i == 0 or s[i - 1].lower() == "e":
                continue
            return False
        
        if c == "e":
            if hasExponential or not hasDigits:
                return False
            hasExponential = True
            hasDecimal = True
            hasDigits = False
            continue

        return False

    return hasDigits


if __name__ == "__main__":
    passedTests = 0
    totalTests = 0

    # Example 1:
    s = "0"
    expected = True
    output = ValidNumber(s)
    print("Example 1")
    print(expected)
    print(output)
    print(expected == output)
    totalTests += 1
    passedTests += 1 if expected == output else 0
    print()

    # Example 2:
    s = "e"
    expected = False
    output = ValidNumber(s)
    print("Example 2")
    print(expected)
    print(output)
    print(expected == output)
    totalTests += 1
    passedTests += 1 if expected == output else 0
    print()

    # Example 3:
    s = "."
    expected = False
    output = ValidNumber(s)
    print("Example 3")
    print(expected)
    print(output)
    print(expected == output)
    totalTests += 1
    passedTests += 1 if expected == output else 0
    print()

    # Example 4
    s = "2"
    expected = True
    output = ValidNumber(s)
    print("Example  4")
    print(expected)
    print(output)
    print(expected == output)
    totalTests += 1
    passedTests += 1 if expected == output else 0
    print()

    # Example 5
    s = "0089"
    expected = True
    output = ValidNumber(s)
    print("Example 5")
    print(expected)
    print(output)
    print(expected == output)
    totalTests += 1
    passedTests += 1 if expected == output else 0
    print()

    # Example 6
    s = "-0.1"
    expected = True
    output = ValidNumber(s)
    print("Example 6")
    print(expected)
    print(output)
    print(expected == output)
    totalTests += 1
    passedTests += 1 if expected == output else 0
    print()

    # Example 7
    s = "+3.14"
    expected = True
    output = ValidNumber(s)
    print("Example 7")
    print(expected)
    print(output)
    print(expected == output)
    totalTests += 1
    passedTests += 1 if expected == output else 0
    print()

    # Example 8
    s = "4."
    expected = True
    output = ValidNumber(s)
    print("Example 8")
    print(expected)
    print(output)
    print(expected == output)
    totalTests += 1
    passedTests += 1 if expected == output else 0
    print()

    # Example 9
    s = "-.9"
    expected = True
    output = ValidNumber(s)
    print("Example 9")
    print(expected)
    print(output)
    print(expected == output)
    totalTests += 1
    passedTests += 1 if expected == output else 0
    print()

    # Example 10
    s = "2e10"
    expected = True
    output = ValidNumber(s)
    print("Example 10")
    print(expected)
    print(output)
    print(expected == output)
    totalTests += 1
    passedTests += 1 if expected == output else 0
    print()

    # Example 11
    s = "-90E3"
    expected = True
    output = ValidNumber(s)
    print("Example 11")
    print(expected)
    print(output)
    print(expected == output)
    totalTests += 1
    passedTests += 1 if expected == output else 0
    print()

    # Example 12
    s = "3e+7"
    expected = True
    output = ValidNumber(s)
    print("Example 12")
    print(expected)
    print(output)
    print(expected == output)
    totalTests += 1
    passedTests += 1 if expected == output else 0
    print()

    # Example 13
    s = "+6e-1"
    expected = True
    output = ValidNumber(s)
    print("Example 13")
    print(expected)
    print(output)
    print(expected == output)
    totalTests += 1
    passedTests += 1 if expected == output else 0
    print()

    # Example 14
    s = "53.5e93"
    expected = True
    output = ValidNumber(s)
    print("Example 14")
    print(expected)
    print(output)
    print(expected == output)
    totalTests += 1
    passedTests += 1 if expected == output else 0
    print()

    # Example 15
    s = "-123.456e789"
    expected = True
    output = ValidNumber(s)
    print("Example 15")
    print(expected)
    print(output)
    print(expected == output)
    totalTests += 1
    passedTests += 1 if expected == output else 0
    print()

    # Example 16
    s = "-123.456e789.2"
    expected = False
    output = ValidNumber(s)
    print("Example 16")
    print(expected)
    print(output)
    print(expected == output)
    totalTests += 1
    passedTests += 1 if expected == output else 0
    print()

    # Example 17
    s = ".25"
    expected = True
    output = ValidNumber(s)
    print("Example 17")
    print(expected)
    print(output)
    print(expected == output)
    totalTests += 1
    passedTests += 1 if expected == output else 0
    print()

    # Example 18
    s = "abc"
    expected = False
    output = ValidNumber(s)
    print("Example 18")
    print(expected)
    print(output)
    print(expected == output)
    totalTests += 1
    passedTests += 1 if expected == output else 0
    print()

    # Example 19
    s = "1a"
    expected = False
    output = ValidNumber(s)
    print("Example 19")
    print(expected)
    print(output)
    print(expected == output)
    totalTests += 1
    passedTests += 1 if expected == output else 0
    print()

    # Example 20
    s = "1e"
    expected = False
    output = ValidNumber(s)
    print("Example 20")
    print(expected)
    print(output)
    print(expected == output)
    totalTests += 1
    passedTests += 1 if expected == output else 0
    print()

    # Example 21
    s = "e3"
    expected = False
    output = ValidNumber(s)
    print("Example 21")
    print(expected)
    print(output)
    print(expected == output)
    totalTests += 1
    passedTests += 1 if expected == output else 0
    print()

    # Example 22
    s = "99e2.5"
    expected = False
    output = ValidNumber(s)
    print("Example 22")
    print(expected)
    print(output)
    print(expected == output)
    totalTests += 1
    passedTests += 1 if expected == output else 0
    print()

    # Example 23
    s = "--6"
    expected = False
    output = ValidNumber(s)
    print("Example 23")
    print(expected)
    print(output)
    print(expected == output)
    totalTests += 1
    passedTests += 1 if expected == output else 0
    print()

    # Example 24
    s = "-+3"
    expected = False
    output = ValidNumber(s)
    print("Example 24")
    print(expected)
    print(output)
    print(expected == output)
    totalTests += 1
    passedTests += 1 if expected == output else 0
    print()

    # Example 25
    s = "95a54e53"
    expected = False
    output = ValidNumber(s)
    print("Example 25")
    print(expected)
    print(output)
    print(expected == output)
    totalTests += 1
    passedTests += 1 if expected == output else 0
    print()

    print("Total tests:", totalTests)
    print("Passed tests:", passedTests)