#include<iostream>
#include<vector>

std::vector<std::vector<int>> AllPermutations(std::vector<int> &nums)
{
    std::vector<std::vector<int>> prevPermutations = {{}};
    std::vector<std::vector<int>> allPermutations = {};

    for (int num : nums)
    {
        allPermutations = {};
        for (std::vector<int> permutation : prevPermutations)
        {
            for (int i = 0; i < permutation.size() + 1; i ++)
            {
                std::vector<int> newPerm = permutation;
                newPerm.insert(newPerm.begin() + i, num);
                allPermutations.push_back(newPerm);
            }
        }
        prevPermutations = allPermutations;
    }

    return allPermutations;
}

void PrintVector(std::vector<int> nums)
{
    std::cout << "{ ";
    for (int num : nums)
    {
        std::cout << num << " ";
    }
    std::cout << "} ";
}

void PrintVectorOfVectors(std::vector<std::vector<int>> vectorOfVectors)
{
    for (std::vector<int> innerVector : vectorOfVectors)
    {
        PrintVector(innerVector);
    }
    std::cout << std::endl;
}

int main()
{
    std::vector<int> nums = {1, 2, 3};
    std::vector<std::vector<int>> output = AllPermutations(nums);

    std::cout << "Sample:" << std::endl;
    PrintVector(nums);

    std::cout << "\n\nAll permutations:" << std::endl;
    PrintVectorOfVectors(output);

    return 0;
}