#include <iostream>
#include <vector>

int BinarySearch(std::vector<int> &nums, int target)
{
    int low = 0;
    int high = nums.size() - 1;

    while (low <= high)
    {
        int mid = (int)((low + high) / 2);

        if (nums[mid] == target)
        {
            return mid;
        }

        if (nums[mid] < target)
        {
            low = mid + 1;
        }
        else // nums[mid] > target
        {
            high = mid - 1;
        }
    }

    return - 1;
}

void PrintVector(std::vector<int> &nums)
{
    for(int num : nums)
    {
        std::cout << num << " ";
    }
    std::cout << std::endl;
}

int main()
{
    std::vector<int> nums = {1, 3, 5, 9, 11, 24, 36};
    int target = 11;
    int expectedOutput = 4;
    int output = BinarySearch(nums, target);
   
    PrintVector(nums);
   
    std::cout << "Target " << target << " found at index " << output << std::endl;
    std::cout << "Output: " << output << std::endl;
    std::cout << "Expected: " << expectedOutput << std::endl;
}