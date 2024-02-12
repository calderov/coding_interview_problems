# Given a sorted unique integer array nums.
# 
# A range [a,b] is the set of all integers from a to b (inclusive).
# 
# Return the smallest sorted list of ranges that cover all the numbers in the
# array exactly. That is, each element of nums is covered by exactly one of
# the ranges, and there is no integer x such that x is in one of the ranges
# but not in nums.
# 
# Each range [a,b] in the list should be output as:
# 
# 'a->b' if a != b
# 'a' if a == b
#  
# Examples:
#   Input: nums = [0,1,2,4,5,7]
#   Output: ['0->2','4->5','7']
#   Explanation: The ranges are:
#   [0,2] --> '0->2'
#   [4,5] --> '4->5'
#   [7,7] --> '7'
#   
#   Input: nums = [0,2,3,4,6,8,9]
#   Output: ['0','2->4','6','8->9']
#   Explanation: The ranges are:
#   [0,0] --> '0'
#   [2,4] --> '2->4'
#   [6,6] --> '6'
#   [8,9] --> '8->9'

def GetInterval(start, end):
    if start == end:
        return f'{start}'
    return f'{start}->{end}'

def SummaryRanges(nums):
    summary = []

    fast = 0
    slow = 0

    while fast < len(nums) - 1:
        if nums[fast] == nums[fast + 1] - 1:
            fast += 1
        else:
            summary.append(GetInterval(nums[slow], nums[fast]))
            slow = fast + 1
            fast = fast + 1
    
    summary.append(GetInterval(nums[slow], nums[fast]))
    
    return summary

if __name__ == '__main__':
    # Example 1
    nums = [0, 1, 2, 4, 5, 7]
    expectedOutput = ['0->2','4->5','7']
    output = SummaryRanges(nums)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 2
    nums = [0, 2, 3, 4, 6, 8, 9]
    expectedOutput = ['0','2->4','6','8->9']
    output = SummaryRanges(nums)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()
