def Partition(nums, low, high):
    pivot = nums[high]
    index = low - 1

    for i in range(low, high):
        if nums[i] <= pivot:
            index += 1
            nums[index], nums[i] = nums[i], nums[index]

    index += 1
    nums[index], nums[high] = nums[high], nums[index]

    return index

def Quicksort(nums, low=None, high=None):
    if low == None and high == None:
        low = 0
        high = len(nums) - 1

    if low < high:
        index = Partition(nums, low, high)
        Quicksort(nums, low, index - 1)
        Quicksort(nums, index + 1, high)

if __name__ == "__main__":
    nums = [1, 5, 4, 2, 7, 3, 10, 8, 9, 6]
    Quicksort(nums)
    print(nums)
