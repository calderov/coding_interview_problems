# Write a function to find the longest common prefix string amongst an array
# of strings.
# 
# If there is no common prefix, return an empty string "".
#  
# Examples:
# 
#   Input: strs = ["flower","flow","flight"]
#   Output: "fl"
# 
#   Input: strs = ["dog","racecar","car"]
#   Output: ""
#   Explanation: There is no common prefix among the input strings.
#  

def GetCommonPrefix(string1, string2):
    n = min(len(string1), len(string2))
    prefix = []
    
    for i in range(n):
        if string1[i] != string2[i]:
            break
        prefix.append(string1[i])
    
    return "".join(prefix)

# Time complexity: O(n * k) where n is the number of strings and k is the length of the longest string
# Space complexity: O(k)
def GetLongestCommonPrefix(strings):
    if not strings:
        return []
    
    longestPrefix = strings[0]
    for i in range(len(strings) - 1):
        prefix = GetCommonPrefix(strings[i], strings[i + 1])
        
        if len(prefix) < len(longestPrefix):
            longestPrefix = prefix

    return prefix

if __name__ == "__main__":
    # Example 1
    strings = ["flower","flow","flight"]
    expectedOutput = "fl"
    output = GetLongestCommonPrefix(strings)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    strings = ["dog","racecar","car"]
    expectedOutput = ""
    output = GetLongestCommonPrefix(strings)
    print(output, expectedOutput, output == expectedOutput)