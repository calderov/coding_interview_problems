# Group Anagrams
# MEDIUM
# Description

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Explanation:
#     There is no string in strs that can be rearranged to form "bat".
#     The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
#     The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

# Constraints:
#     1 <= strs.length <= 104
#     0 <= strs[i].length <= 100
#     strs[i] consists of lowercase English letters.

# Time: O(n * k * log(k)) where k is the lenght of the longest word in words
# Space: O(n * k)
def GroupAnagrams(words):
    anagrams = {}
    for word in words:
        wordKey = "".join(sorted([c for c in word]))
        if wordKey not in anagrams:
            anagrams[wordKey] = []
        anagrams[wordKey].append(word)
    return anagrams.values()

if __name__ == "__main__":
    # Example 1:
    words = ["eat","tea","tan","ate","nat","bat"]
    expected = [["bat"],["nat","tan"],["ate","eat","tea"]]
    output = GroupAnagrams(words)
    sortedExpected = sorted([sorted(g) for g in expected], key=len)
    sortedOutput = sorted([sorted(g) for g in output], key=len)
    print(sortedExpected)
    print(sortedOutput)
    print(sortedExpected == sortedOutput)
    print()

    # Example 2:
    words = [""]
    expected = [[""]]
    output = GroupAnagrams(words)
    sortedExpected = sorted([sorted(g) for g in expected], key=len)
    sortedOutput = sorted([sorted(g) for g in output], key=len)
    print(sortedExpected)
    print(sortedOutput)
    print(sortedExpected == sortedOutput)
    print()

    # Example 3:
    words = ["a"]
    expected = [["a"]]
    output = GroupAnagrams(words)
    sortedExpected = sorted([sorted(g) for g in expected], key=len)
    sortedOutput = sorted([sorted(g) for g in output], key=len)
    print(sortedExpected)
    print(sortedOutput)
    print(sortedExpected == sortedOutput)
    print()

    # Example 4: Multiple words that are all anagrams
    words = ["abc", "bac", "cab", "cba", "acb", "bca"]
    expected = [["abc", "bac", "cab", "cba", "acb", "bca"]]
    output = GroupAnagrams(words)
    sortedExpected = sorted([sorted(g) for g in expected], key=len)
    sortedOutput = sorted([sorted(g) for g in output], key=len)
    print(sortedExpected)
    print(sortedOutput)
    print(sortedExpected == sortedOutput)
    print()

    # Example 5: No anagrams (all unique words)
    words = ["apple", "banana", "cherry", "dog"]
    expected = [["apple"], ["banana"], ["cherry"], ["dog"]]
    output = GroupAnagrams(words)
    sortedExpected = sorted([sorted(g) for g in expected], key=len)
    sortedOutput = sorted([sorted(g) for g in output], key=len)
    print(sortedExpected)
    print(sortedOutput)
    print(sortedExpected == sortedOutput)
    print()

    # Example 6: Mix of single and multi-character words
    words = ["a", "b", "ab", "ba", "abc", "c"]
    expected = [["a"], ["b"], ["ab", "ba"], ["abc"], ["c"]]
    output = GroupAnagrams(words)
    sortedExpected = sorted([sorted(g) for g in expected], key=len)
    sortedOutput = sorted([sorted(g) for g in output], key=len)
    print(sortedExpected)
    print(sortedOutput)
    print(sortedExpected == sortedOutput)
    print()

    # Example 7: Words with duplicate letters
    words = ["aabb", "abab", "baba", "xyzz", "zzyx"]
    expected = [["aabb", "abab", "baba"], ["xyzz", "zzyx"]]
    output = GroupAnagrams(words)
    sortedExpected = sorted([sorted(g) for g in expected], key=len)
    sortedOutput = sorted([sorted(g) for g in output], key=len)
    print(sortedExpected)
    print(sortedOutput)
    print(sortedExpected == sortedOutput)
    print()

    # Example 8: Single word
    words = ["hello"]
    expected = [["hello"]]
    output = GroupAnagrams(words)
    sortedExpected = sorted([sorted(g) for g in expected], key=len)
    sortedOutput = sorted([sorted(g) for g in output], key=len)
    print(sortedExpected)
    print(sortedOutput)
    print(sortedExpected == sortedOutput)
    print()

    # Example 9: Two groups of anagrams
    words = ["listen", "silent", "enlist", "hello", "world"]
    expected = [["listen", "silent", "enlist"], ["hello"], ["world"]]
    output = GroupAnagrams(words)
    sortedExpected = sorted([sorted(g) for g in expected], key=len)
    sortedOutput = sorted([sorted(g) for g in output], key=len)
    print(sortedExpected)
    print(sortedOutput)
    print(sortedExpected == sortedOutput)
    print()