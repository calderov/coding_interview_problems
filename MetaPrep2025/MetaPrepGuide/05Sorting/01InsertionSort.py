# Insertion Sort - Part 2
# https://www.hackerrank.com/challenges/insertionsort2/problem

def insertionSort(nums):
    # Remove next line to run in place
    nums = [d for d in nums]

    n = len(nums)
    for i in range(1, n):
        key = nums[i]
        j = i - 1

        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = key
    
    return nums

if __name__=="__main__":
    nums = [3,4,2,1,5]
    expected = [1,2,3,4,5]
    output = insertionSort(nums)
    
    print(nums)
    print(expected)
    print(output)
    print(output == expected)
    