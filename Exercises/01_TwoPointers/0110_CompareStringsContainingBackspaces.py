# Problem:
# Given two strings containing backspaces (identified by the character ‘#’),
# check if the two strings are equal.
#
# Example:
# Input: string1 = "xy#z", string2 = "xzz#"
# Output: true
# Explanation: After applying backspaces the strings become "xz" and "xz" respectively.

# Solution 1:
# For each of the input strings, use a stack to produce a new string without the backspace
# characters and without the characters that should be affected by them. Then compare these
# new strings and return True if they are equal or False otherwise.
#
# Solution 1 complexity:
# Time complexity: O(n) where n is the number of characters in string1 and string2 combined.
# Space complexity: O(n) as the underlying stacks could potentially contain all the characters in string1 and string2.
def ApplyBackspaces(string):
    stack = []
    for c in string:
        if c == '#':
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(c)
    return ''.join(stack)

def CompareStringsContainingBackspaces(string1, string2):
    return ApplyBackspaces(string1) == ApplyBackspaces(string2)

# Solution 2:
# Use two pointers i and j to traverse the input strings string1 and string2 respectively.
# Start by initializing i and j to point at the last positions of string1 and string2,
# so we traverse the strings backwards in search of backspace characters. I.e:
#   i = len(string1) - 1
#   j = len(string2) - 1
# 
# While both i and j are greater or equal than zero, check if the i or j are pointing to
# a backspace character (#). If so, move them to the next viable position on their respective
# string, otherwise, it means that they are in a valid character already.
#
# Now compare the values pointed by i and j, if they are different return False now
# as we have found that removing the backspaces this far has revealed a difference
# in the strings. Otherwise, move both pointers to the left.
#
# If i and j are both equal to -1 it means that both pointers traversed their respective
# strings without finding differences. Thus the input strings turn equal despite their
# backspaces.
#
# Solution 2 complexity:
# Time complexity: O(n) where n is the number of characters in string1 and string2 combined.
# Space complexity: O(1) constant as no additional data structure is required to solve this, only a few pointers.
def GetNextValidIndex(string, index):
    remove = 2
    while remove:
        index -= 1
        remove -= 1
        
        # If no more valid characters are left in the string return -1
        if index < 0:
            return -1
        
        if string[index] == '#':
            remove += 2
    return index

def CompareStringsContainingBackspacesV2(string1, string2):
    i = len(string1) - 1
    j = len(string2) - 1

    while i >= 0 and j >= 0:
        if string1[i] == '#':
            i = GetNextValidIndex(string1, i)

        if string2[j] == '#':
            j = GetNextValidIndex(string2, j)

        # Return False if any of the two strings got depleted early
        if (i == -1 and j != -1) or (i != -1 and j == -1):
            return False

        if string1[i] != string2[j]:
            return False

        i -= 1
        j -= 1

    return True

if __name__ == "__main__":
    # Example 1:
    string1 = "xy#z"
    string2 = "xzz#"
    expectedOutput = True
    output = CompareStringsContainingBackspacesV2(string1, string2)
    print(output, expectedOutput, "\n")

    # Example 2:
    string1 = "xy#z"
    string2 = "xyz#"
    expectedOutput = False
    output = CompareStringsContainingBackspacesV2(string1, string2)
    print(output, expectedOutput, "\n")

    # Example 3:
    string1 = "xp#"
    string2 = "xyz##"
    expectedOutput = True
    output = CompareStringsContainingBackspacesV2(string1, string2)
    print(output, expectedOutput, "\n")

    # Example 4:
    string1 = "xywrrmp"
    string2 = "xywrrmu#p"
    expectedOutput = True
    output = CompareStringsContainingBackspacesV2(string1, string2)
    print(output, expectedOutput, "\n")

    # Example 5:
    string1 = "abc#"
    string2 = "abc##"
    expectedOutput = False
    output = CompareStringsContainingBackspacesV2(string1, string2)
    print(output, expectedOutput, "\n")

    # Example 6:
    string1 = "#"
    string2 = "#"
    expectedOutput = True
    output = CompareStringsContainingBackspacesV2(string1, string2)
    print(output, expectedOutput, "\n")