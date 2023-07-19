# Problem:
# A pangram is a sentence where every letter of the English alphabet appears at least once.
#
# Given a string sentence containing English letters (lower or upper-case), return True if 
# the sentence is a pangram, or False otherwise. Digits, spaces and special characters should
# be handled too.
#
# For example:
# - The sentence "TheQuickBrownFoxJumpsOverTheLazyDog" is a pangram. Thus, when passed to the IsPangram function, it should return True.
# - The sentence "This is not a pangram" is not a pangram. Thus, when passed to the IsPangram function, it should return False.

# Solution:
# Use a hash set to store all the lower-case English letters, then traverse the sentence one character at a time
# removing its lower case version from the set and checking if this made the set is empty. If the set is empty 
# return True, as it means that all the characters in the English letters set have been "seen" at least once in the
# sentence, making it a pangram. Otherwise, continue until we finish traversing the sentence. If the end of the sentence 
# is reached and there are still characters in the set, return False.
#
# Solution complexity:
# Time complexity: O(n) where n is the number of elements in the array.
# Space complexity: O(1) constant space.
def IsPangram(sentence):
    charSet = set([i for i in "abcdefghijklmnopqrstuvwxyz"])
    for c in sentence:
        if c.lower() in charSet:
            charSet.remove(c.lower())
        if len(charSet) == 0:
            return True
    return False

if __name__ == "__main__":
    example = "TheQuickBrownFoxJumpsOverTheLazyDog"
    print(IsPangram(example), True)

    example = "This is not a pangram"
    print(IsPangram(example), False)