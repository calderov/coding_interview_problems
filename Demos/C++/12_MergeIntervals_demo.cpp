#include <iostream>
#include <algorithm>
#include <vector>

bool IsOverlap(std::vector<int> intervalA, std::vector<int> intervalB)
{
    return !(intervalA.back() < intervalB.front() || intervalB.back() < intervalA.front());
}

std::vector<int> Merge(std::vector<int> intervalA, std::vector<int> intervalB)
{
    int start = std::min(intervalA.front(), intervalB.front());
    int end = std::max(intervalA.back(), intervalB.back());
    return {start, end};
}

std::vector<std::vector<int>> MergeIntervals(std::vector<std::vector<int>> intervals)
{
    std::vector<std::vector<int>> mergedIntervals = {};
    
    std::sort(intervals.begin(), intervals.end());

    for (std::vector<int> interval : intervals)
    {
        if (mergedIntervals.size() == 0 || !IsOverlap(mergedIntervals.back(), interval))
        {
            mergedIntervals.push_back(interval);
        }
        else
        {
            mergedIntervals.back() = Merge(mergedIntervals.back(), interval);
        }
    }

    return mergedIntervals;
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
    std::vector<std::vector<int>> intervals = {{1, 4}, {2, 5}, {7, 9}};
    std::vector<std::vector<int>> expectedOutput = {{1, 5}, {7, 9}};
    std::vector<std::vector<int>> output = MergeIntervals(intervals);
    bool success = output == expectedOutput;

    std::cout << "Input intervals:" << std::endl;
    PrintVectorOfVectors(intervals);

    std::cout << "\nMerged intervals:" << std::endl;
    PrintVectorOfVectors(output);

    std::cout << "\nExpected output:" << std::endl;
    std::cout << success << std::endl;
}