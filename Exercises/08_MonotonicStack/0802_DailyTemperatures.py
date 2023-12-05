# Problem:
# Given an array of integers temperatures representing daily temperatures,
# your task is to calculate how many days you have to wait until a warmer
# temperature. If there is no future day for which this is possible, put 0
# instead.
#
# Example:
#
#   Input: temperatures = [70, 73, 75, 71, 69, 72, 76, 73]
#   Output: [1, 1, 4, 2, 1, 1, 0, 0]
#
#   Explanation: The first day's temperature is 70 and the next day's
#   temperature is 73 which is warmer. So for the first day, you only have to
#   wait for 1 day to get a warmer temperature. Hence, the first element in the
#   result array is 1. The same process is followed for the rest of the days.
#

class Solution:
    # Solution:
    # Brute force. Compare the temperature of every day with that of all the subsequent days in the array.
    # If a greater one is found, compute the distance in days between the greater temperature day and the
    # current day, add it to the answer and continue.
    # 
    # Solution complexity:
    # Time complexity: O(n ^ 2)
    # Space complexity: O(n)
    def DaysUntilWarmerV1(self, temperatures):
        days = []
        for i in range(len(temperatures)):
            count = 0
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    count = j - i
                    break

            days.append(count)

        return days

    # Solution:
    # 1. Initialize an empty stack to store the indices of the temperatures
    #    array. Also, initialize a result array of the same length as temperatures
    #    with all values set to 0.
    #   
    # 2. Iterate over the temperatures array. For each temperature:
    #   
    #   2.1. While the stack is not empty and the current temperature is greater
    #      than the temperature at the index on the top of the stack, set the value in
    #      the result array at the top index of the stack to the difference between
    #      the current index and the top index of the stack. Pop the index from the
    #      stack.
    #   
    #   2.2. Push the current index onto the stack.
    # 
    # 3. Return the result array.
    # 
    # Solution complexity:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def DaysUntilWarmerV2(self, temperatures):
        days = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                days[stack[-1]] = i - stack[-1]
                stack.pop()

            stack.append(i)

        return days

    def DaysUntilWarmer(self, temperatures):
        return self.DaysUntilWarmerV2(temperatures)

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    temperatures = [70, 73, 75, 71, 69, 72, 76, 73]
    expectedOutput = [1, 1, 4, 2, 1, 1, 0, 0]
    output = solution.DaysUntilWarmer(temperatures)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 1
    temperatures = [73, 72, 71, 70]
    expectedOutput = [0, 0, 0, 0]
    output = solution.DaysUntilWarmer(temperatures)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 1
    temperatures = [70, 71, 72, 73]
    expectedOutput = [1, 1, 1, 0]
    output = solution.DaysUntilWarmer(temperatures)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()
