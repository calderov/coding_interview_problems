#include <iostream>
#include <vector>

void Swap(std::vector<int> &nums, int i, int j)
{
    int temp = nums[i];
    nums[i] = nums[j];
    nums[j] = temp;
}

int Partition(std::vector<int> &nums, int low, int high)
{
    int pivot = nums[high];
    int index = low - 1;

    for (int i = low; i < high; i++)
    {
        if (nums[i] <= pivot)
        {
            index++;
            Swap(nums, i, index);
        }
    }

    index++;
    Swap(nums, index, high);

    return index;
}

void QuickSort(std::vector<int> &nums, int low=-1, int high=-1)
{
    if (low == -1 && high == -1)
    {
        low = 0;
        high = nums.size() - 1;
    }

    if (low < high)
    {
        int index = Partition(nums, low, high);
        QuickSort(nums, low, index - 1);
        QuickSort(nums, index + 1, high);
    }
}

void PrintVector(std::vector<int> &nums)
{
    for (int element: nums)
    {
        std::cout << element << " ";
    }
    std::cout << std::endl;
}

int main()
{
    std::vector<int> nums = {1, 5, 4, 2, 7, 3, 10, 8, 9, 6};
    PrintVector(nums);
    QuickSort(nums);
    PrintVector(nums);
    return 0;
}