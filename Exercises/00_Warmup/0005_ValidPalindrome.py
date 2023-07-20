# Problem:
# Given a string s, return True if it is a palindrome, or False otherwise.
#  
# Solution:
# First, copy the contents of the input string into a list, dropping all the spaces and
# non-alphanumeric characters. Then, place two pointers, one on the first position
# of the list (left) and one on the last (right).
# While the left pointer is lesser or equal to the right one, compare the values they
# are pointing to. If these values are equal, move the left pointer to the right and
# the right pointer to the left, and repeat. If at any point the pointed values differ,
# return False. Otherwise return True once the pointers converge in the middle of the list.
def IsPalindrome(s):
    S = [i.lower() for i in s if i.isalpha() or i.isdigit()]
    left = 0
    right = len(S) - 1
    while left <= right:
        if S[left] == S[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

if __name__ == "__main__":
    print(IsPalindrome("A man, a plan, a canal, Panama!"))
    print(IsPalindrome("race a car"))
    print(IsPalindrome("Was it a car or a cat I saw?"))
    print(IsPalindrome("12345"))