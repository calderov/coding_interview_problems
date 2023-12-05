# Problem:
# Given a list of strings, the task is to group the anagrams together.
# 
# An anagram is a word or phrase formed by rearranging the letters of
# another, such as "cinema", formed from "iceman".
# 
# Examples:
# 
#   Example 1:
#   Input: ["dog", "god", "hello"]
#   Output: [["dog", "god"], ["hello"]]
#   Justification: "dog" and "god" are anagrams, so they are grouped together.
#                  "hello" does not have any anagrams in the list, so it is in its own group.
# 
#   Example 2:
#   Input: ["listen", "silent", "enlist"]
#   Output: [["listen", "silent", "enlist"]]
#   Justification: All three words are anagrams of each other, so they are
#                  grouped together.
# 
#   Example 3:
#   Input: ["abc", "cab", "bca", "xyz", "zxy"]
#   Output: [["abc", "cab", "bca"], ["xyz", "zxy"]]
#   Justification: "abc", "cab", and "bca" are anagrams, as are "xyz" and "zxy".

class Solution:
    # Time complexity: 
    # Space complexity: 
    def GroupAnagrams(self, words):
        groupMaps = {}

        for word in words:
            key = ''.join(sorted([i for i in word]))
            
            if key not in groupMaps:
                groupMaps[key] = []

            groupMaps[key].append(word)

        return [groupMaps[key] for key in groupMaps]

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    words = ["dog", "god", "hello"]
    expectedOutput = [["dog", "god"], ["hello"]]
    output = solution.GroupAnagrams(words)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()
  
    # Example 2
    words = ["listen", "silent", "enlist"]
    expectedOutput = [["listen", "silent", "enlist"]]
    output = solution.GroupAnagrams(words)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()
  
    # Example 3
    words = ["abc", "cab", "bca", "xyz", "zxy"]
    expectedOutput = [["abc", "cab", "bca"], ["xyz", "zxy"]]
    output = solution.GroupAnagrams(words)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()