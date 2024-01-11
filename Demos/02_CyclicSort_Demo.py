def CyclicSort(nums):
    i = 0
    while i < len(nums):
        if nums[i] != nums[nums[i] - 1]:
            j = nums[i] - 1
            nums[i], nums[j] = nums[j], nums[i]
            continue
        i += 1

# This version of the algorithm allows numbers outside the [1, n] range (negatives, 
# zero and numbers greater than n).
#
# Time complexity: O(n)
# Space complexity: O(1)
def CyclicSortExtended(self, nums):
    i = 0
    while i < len(nums):
        if nums[i] > 0 and \
           nums[i] <= len(nums) and \
           nums[i] != nums[nums[i] - 1]:
            j = nums[i] - 1
            nums[i], nums[j] = nums[j], nums[i]
            continue
        i += 1

if __name__ == "__main__":
    nums = [2, 1, 4, 5, 3]
    print(nums)

    CyclicSort(nums)
    print(nums)
