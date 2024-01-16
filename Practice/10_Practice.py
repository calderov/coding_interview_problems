# Given an array of unsorted numbers return the second largest one
def GetSecondLargest(nums):
    if not nums or len(nums) < 2:
        return None
    
    largest = []

    for num in nums:
        if not largest:
            largest.append(num)
            continue

        if len(largest) == 1:
            if num > largest[0]:
                largest.append(num)
            if num < largest[0]:
                largest.insert(0, num)
            continue
        
        if num > largest[-1]:
            largest.pop(0)
            largest.append(num)

    if len(largest) < 2:
        return None

    return largest[0]


print(GetSecondLargest([]), None)
print(GetSecondLargest([1]), None)
print(GetSecondLargest([1, 1]), None)
print(GetSecondLargest([1, 1, 1]), None)
print(GetSecondLargest([1,2,3,4]), 3)
print(GetSecondLargest([4,3,2,1]), 3)
print(GetSecondLargest([4,4,3,2,1]), 3)
