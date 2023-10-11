# Problem:
# Given a string, find all of its permutations preserving the character
# sequence but changing case.
# 
# Examples:
# 
#   Input: "ad52"
#   Output: "ad52", "Ad52", "aD52", "AD52"
# 
#   Input: "ab7c"
#   Output: "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"
# 

class Solution:
    # Solution:
    # 1. Let n be the length of the input string.
    #      n = len(inputString)
    #
    # 2. Create a list of strings representing binary numbers from 0 to 2 ^ n.
    #    Lets call this list binaryTransforms. E.g. for n = 3 the there will 
    #    be 2 ^ 3 = 8 elements in the binaryTransforms list.
    #
    #      binaryTransforms = ['000', '001', '010', '011', '100', '101', '110', '111']
    #
    #    The idea is that each of these transforms should be of the same length than
    #    the input string, so they can be used to produce case permutations. This should
    #    be done by switching the case of each character on the input string to upper case 
    #    its corresponding character in the transform is 1 or to lower case if the its
    #    corresponding character is 0. 
    #    
    #    For example:
    #       inputString = "foo"
    #         transform = "100"
    #      ---------------------
    #       permutation = "Foo"
    #       
    # 3. Initialize an empty set to store our case permutations.
    #      permutations = set()
    #
    # 4. For each transform in the binaryTransforms list, apply
    #    the transform to the input string and add the result to
    #    the permutations set.
    #
    # 5. Cast the permutations set into a list, have it sorted (optional),
    #    and return it.
    #
    # Solution complexity:
    # Time complexity: O(n * 2 ^ n) where n is the length of the input string
    # Space complexity: O(n * 2 ^ n)
    def CasePermutations(self, inputString):
        # Compute binary transforms
        n = len(inputString)
        binaryTransforms = [bin(i)[2:].zfill(n) for i in range(2 ** n)]

        # Compute permutations by applying binary transforms
        permutations = set()
        for transform in binaryTransforms:
            permutations.add(self.ApplyTransform(inputString, transform))

        # Sort (optional) the list of permutations and return it
        return sorted(list(permutations), reverse=True)
    
    def ApplyTransform(self, inputString, transform):
        stringArray = [inputString[i] for i in range(len(inputString))]
        
        for i in range(len(transform)):
            if transform[i] == '1':
                stringArray[i] = stringArray[i].upper()
            else:
                stringArray[i] = stringArray[i].lower()

        return ''.join(stringArray)

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    inputString = "ad52"
    expectedOutput = ['ad52', 'aD52', 'Ad52', 'AD52']
    output = solution.CasePermutations(inputString)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 2
    inputString = "ab7c"
    expectedOutput = ['ab7c', 'ab7C', 'aB7c', 'aB7C', 'Ab7c', 'Ab7C', 'AB7c', 'AB7C']
    output = solution.CasePermutations(inputString)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()
