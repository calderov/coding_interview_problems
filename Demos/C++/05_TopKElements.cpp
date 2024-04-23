#include <queue>
#include <vector>
#include <iostream>

std::vector<int> TopKElements(std::vector<int> &nums, int k)
{
    std::priority_queue<int> max_heap;
    std::vector<int> topK;

    for (int num : nums)
    {
        max_heap.push(num);
    }

    for (int i = 0; i < k; i++)
    {
        topK.push_back(max_heap.top());
        max_heap.pop();
    }

    return topK;
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
    std::vector<int> nums =  {1, 5, 4, 2, 7, 3, 10, 8, 9, 6};
    int k = 4;

    std::cout << "Original vector:\n";
    PrintVector(nums);

    std::cout << "\nTop " << k << " elements\n";
    std::vector<int> topK = TopKElements(nums, k);
    PrintVector(topK);

    return 0;
}