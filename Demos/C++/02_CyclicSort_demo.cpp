#include <iostream>
#include <vector>

void Swap(std::vector<int> &nums, int i, int j)
{
    int temp = nums[i];
    nums[i] = nums[j];
    nums[j] = temp;
}

void CyclicSort(std::vector<int> &nums)
{
    int i = 0;
    while (i < nums.size())
    {
        if (nums[i] != nums[nums[i] - 1])
        {
            int j = nums[i] - 1;
            Swap(nums, i, j);
            continue;
        }
        i++;
    }
}

void PrintVector(std::vector<int> nums)
{
    for (int num : nums) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
}

int main()
{
    // Example 1
    std::vector<int> nums1 = {2, 1, 4, 5, 3};
    PrintVector(nums1);
    CyclicSort(nums1);
    PrintVector(nums1);

    std::cout << std::endl;

    // Example 2 (one missing, one repetition)
    std::vector<int> nums2 = {1, 3, 4, 2, 2};
    PrintVector(nums2);
    CyclicSort(nums2);
    PrintVector(nums2);

    return 0;
}