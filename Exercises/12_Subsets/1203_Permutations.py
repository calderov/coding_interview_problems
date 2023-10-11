# Problem:
# Given a set of distinct numbers, find all of its permutations.
# 
# Permutation is defined as the re-arranging of the elements of the set. For
# example, {1, 2, 3} has the following six permutations:
# 
# {1, 2, 3} {1, 3, 2} {2, 1, 3} {2, 3, 1} {3, 1, 2} {3, 2, 1} If a set has
# ‘n’ distinct elements it will have n!n! permutations.
# 
# Example:
# 
#   Input: [1,3,5]
#   Output: [1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]
# 

class Solution:
    # Solution:
    # 1.Start with an empty list called prevPermutations containing only an empty set.
    #     prevPermutations = [[]]
    #
    # 2. For each number in the input list nums:
    # 
    #    2.1 Initialize an empty list of permutations. 
    #      permutations = []
    #    
    #    2.2 Generate new permutations by inserting the current number at all possible
    #       positions in the existing permutations (prevPermutations), and appending them
    #       at the end of the permutations list.
    #
    #    2.3 Make prevPermutations = permutations once all of the previous permutations have been
    #       traversed.
    #
    #    2.4 Repeat step 2 untill all the numbers in the input have been traversed.
    #
    # 3. Sort the permutations list (optional).
    #
    # 4. Return the permutations list an finish.
    #
    # Solution complexity:
    # Time complexity: O(N*N!) where N is the number of elements in the input list, as there are N! permutations of length N.
    # Space complexity: O(N*N!).
    def AllPermutations(self, nums):
        prevPermutations = [[]]
        permutations = []

        for num in nums:
            permutations = []
            for perm in prevPermutations:
                for i in range(len(perm) + 1):
                    newPerm = perm.copy()
                    newPerm.insert(i, num)
                    permutations.append(newPerm)
            
            prevPermutations = permutations

        permutations.sort()
        return permutations

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [1,3,5]
    expectedOutput = [[1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]]
    output = solution.AllPermutations(nums)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()