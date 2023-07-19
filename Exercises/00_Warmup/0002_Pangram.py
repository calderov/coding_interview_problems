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
# Traverse the sentence one character at a time. For each character check if it is an English letter. If so, add it to an auxiliary
# set so all the different English letters in the sentence are stored in there. Finally check if the cardinality of this auxiliary
# set equals 26, as that is the total number of different English letters.
#
# Solution complexity:
# Time complexity: O(n) where n is the number of elements in the array.
# Space complexity: O(1) constant space.
def IsPangram(sentence):
    englishLettersSet = set()
    for c in sentence:
        if c.isalpha():
            englishLettersSet.add(c.lower())
    return len(englishLettersSet) == 26

if __name__ == "__main__":
    example = "TheQuickBrownFoxJumpsOverTheLazyDog"
    print(IsPangram(example), True)

    example = "This is not a pangram"
    print(IsPangram(example), False)