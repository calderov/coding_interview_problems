#include <iostream>
#include <vector>

std::vector<std::vector<int>> AllSubsets(std::vector<int> nums)
{
    std::vector<std::vector<int>> subsets = {{}};

    for (int num : nums)
    {
        int n = subsets.size();
        for (int i = 0; i < n; i++)
        {
            std::vector<int> subset;
            subset = subsets[i];
            subset.push_back(num);

            subsets.push_back(subset);
        }
    }

    return subsets;
}

void PrintVector(std::vector<int> nums)
{
    for (int num : nums)
    {
        std::cout << num << " ";
    }
}

void PrintVectorOfVectors(std::vector<std::vector<int>> vectorOfVectors)
{
    for (std::vector<int> innerVector : vectorOfVectors)
    {
        std::cout << "{ ";
        PrintVector(innerVector);
        std::cout << "} ";
    }
}

int main()
{
    std::vector<int> nums = {1, 2, 3};
    std::vector<std::vector<int>> expectedOutput =  {{}, {1}, {2}, {1, 2}, {3}, {1, 3}, {2, 3}, {1, 2, 3}};
    std::vector<std::vector<int>> output = AllSubsets(nums);
    
    std::cout << "Sample set { ";
    PrintVector(nums);
    std::cout << "}\n\n";

    std::cout << "Expected subsets:\n";
    PrintVectorOfVectors(expectedOutput);

    std::cout << "\n" << std::endl;

    std::cout << "Computed subsets:\n";
    PrintVectorOfVectors(output);
    return 0;
}