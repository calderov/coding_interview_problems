# Given an array nums containing n distinct numbers in the range 0 to n,
# return the only number from the range 0 that is missing from the array

def MissingNumber(nums):
    xor = len(nums)

    for i in range(len(nums)):
        xor = xor ^ i ^ nums[i]

    return xor

if __name__ == "__main__":
    nums = [3, 0, 1]

    print(MissingNumber(nums))

