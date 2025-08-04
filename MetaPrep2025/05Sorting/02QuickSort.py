# Quicksort 2 - Sorting
# https://www.hackerrank.com/challenges/quicksort2/problem

def partition(nums, low, high):
    pivot = nums[high]
    index = low - 1

    for i in range(low, high):
        if nums[i] <= pivot:
            index += 1
            nums[index], nums[i] = nums[i], nums[index]

    index += 1
    nums[index], nums[high] = nums[high], nums[index]

    return index

def quicksort(nums, low=None, high=None):
    if low == None and high == None:
        low = 0
        high = len(nums) - 1

    if low < high:
        index = partition(nums, low, high)
        quicksort(nums, low, index - 1)
        quicksort(nums, index + 1, high)

if __name__=="__main__":
    nums = [3,4,2,1,5]
    expected = [1,2,3,4,5]
    output = [d for d in nums]
    quicksort(output)
    
    print(nums)
    print(expected)
    print(output)
    print(output == expected)