def BinarySearch(nums, value):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == value:
            return mid
        
        if nums[mid] < value:
            left = mid + 1

        else: # nums[mid] > value
            right = mid - 1
    
    return -1

if __name__ == "__main__":
    nums = [1, 3, 5, 9, 11, 24, 36]
    target = 11
    expectedOutput = 4
    output = BinarySearch(nums, target)
    print(output, expectedOutput, output == expectedOutput)