
def CyclicSort(nums):
    i = 0
    while i < len(nums):
        if nums[i] != nums[nums[i] - 1]:
            j = nums[i] - 1
            nums[i], nums[j] = nums[j], nums[i]
            continue
        i += 1

if __name__ == "__main__":
    nums = [2, 1, 4, 5, 3]
    print(nums)

    CyclicSort(nums)
    print(nums)