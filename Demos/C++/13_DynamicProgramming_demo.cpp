#include <iostream>
#include <vector>

// Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number ‘S’.
//
// Time complexity: O(n * s)
// Space complexity: O(n * s)
int TotalNumberOfSubsetsWithSumS(std::vector<int> nums, int s)
{
    int rows = nums.size();
    int cols = s + 1;

    // Initialize the dynamic programming table (dp)
    std::vector<std::vector<int>> dp;
    for (int row = 0; row < rows; row++)
    {
        dp.push_back({});
        for (int col = 0; col < cols; col++)
        {
            dp.back().push_back(0);
        }
    }

    // Base case: Mark the fist colum as every set has an empty set that adds up to zero.
    for (int row = 0; row < rows; row++)
    {
        dp[row][0] = 1;
    }
    
    // Base case: A set containing only the first element from nums can add up to the value
    //            of the first element of nums, mark its corresponding colum.
    if (nums[0] < cols)
    {
        dp[0][nums[0]] = 1;
    }

    // For each cell on the dynamic programming table
    for (int row = 1; row < rows; row++)
    {
        for (int col = 1; col < cols; col++)
        {
            int element = nums[row];

            // Case 1: Exclude the current element
            dp[row][col] += dp[row - 1][col];

            // Case 2: Include the current element
            if (col >= element)
            {
                dp[row][col] += dp[row - 1][col - element];
            }
        }
    }
    
    // The amount of subsets that add up to S is located
    // in the last cell of the dynamic programming table
    return dp.back().back();
}

int main()
{
    std::vector<int> nums = {1, 2, 7, 1, 5};
    int s = 9;
    int expectedOutput = 3; // The given set has 3 subsets whose sum is 9:
                            // {2, 7}, {1, 7, 1}, {1, 2, 1, 5}
    int output = TotalNumberOfSubsetsWithSumS(nums, s);
    bool success = output == expectedOutput;

    std::cout << "Output: " << output << std::endl;
    std::cout << "Expected output: " << expectedOutput << std::endl;
    std::cout << "\nSuccess: " << success << std::endl;
}