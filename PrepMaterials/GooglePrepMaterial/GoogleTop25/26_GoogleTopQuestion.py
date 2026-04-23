# Add Binary
# EASY
# https://scaleengineer.com/dsa/problems/add-binary

# Description
# Given two binary strings a and b, return their sum as a binary string.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"

# Constraints:
#     1 <= a.length, b.length <= 104
#     a and b consist only of '0' or '1' characters.
#     Each string does not contain leading zeros except for the zero itself.

# Time: O(max(m,n))
# Space: O(max(m,n))
def AddBinary(a, b):
    result = []
    digit = 0
    carry = 0

    i = len(a) - 1
    j = len(b) - 1

    while i >= 0 or j >= 0:
        d1 = int(a[i]) if i >= 0 else 0
        d2 = int(b[j]) if j >= 0 else 0
        digit = (d1 + d2 + carry) % 2
        carry = (d1 + d2 + carry) // 2
        result.append(str(digit))
        i -= 1
        j -= 1

    if carry:
        result.append(str(carry))
    
    result.reverse()

    return "".join(result)

if __name__=="__main__":
    # Example 1:
    a = "11"
    b = "1"
    expected = "100"
    output = AddBinary(a, b)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 2:
    a = "1010"
    b = "1011"
    expected = "10101"
    output = AddBinary(a, b)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 3: Single digit zeros
    a = "0"
    b = "0"
    expected = "0"
    output = AddBinary(a, b)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 4: Single digit ones (produces carry)
    a = "1"
    b = "1"
    expected = "10"
    output = AddBinary(a, b)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 5: Different lengths
    a = "0"
    b = "1"
    expected = "1"
    output = AddBinary(a, b)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 6: All ones (produces carry)
    a = "1111"
    b = "1111"
    expected = "11110"
    output = AddBinary(a, b)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 7: Larger binary numbers
    a = "1"
    b = "111"
    expected = "1000"
    output = AddBinary(a, b)
    print(expected)
    print(output)
    print(expected == output)
    print()