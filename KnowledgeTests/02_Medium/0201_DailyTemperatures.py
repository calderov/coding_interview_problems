# Problem:
# You are given a list of daily temperatures. Your task is to return an
# answer array such that answer[i] is the number of days you would have to
# wait until a warmer temperature for each of the days. If there is no future
# day for which this is possible, put 0 instead.
# 
# Examples
#   Input: [45, 50, 40, 60, 55]
#   Expected Output: [1, 2, 1, 0, 0]
#   Justification: The next day after the first day is warmer (50 > 45). Two
#                  days after the second day, the temperature is warmer (60 > 50).. The next
#                  day after the third day is warmer (60 > 40). There are no warmer days after
#                  the fourth and fifth days.
#   
#   Input: [80, 75, 85, 90, 60]
#   Expected Output: [2, 1, 1, 0, 0]
#   Justification: Two days after the first day, the temperature is warmer (85
#                  > 80). The next day after the second day is warmer (85 > 75). The next day
#                  after the third day is warmer (90 > 85). There are no warmer days after the
#                  fourth and fifth days.
#   
#   Input: [32, 32, 32, 32, 32]
#   Expected Output: [0, 0, 0, 0, 0]
#   Justification: All the temperatures are the same, so there are no warmer
#                  days ahead.

class Solution:
    # Time complexity: O(n ^ 2)
    # Space complexity: O(n)
    def DaysUntilWarmerV1(self, temperatures):
        days = len(temperatures)
        daysUntilWarmer = [0] * days

        for i in range(days):
            for j in range(i + 1, days):
                if temperatures[i] < temperatures[j]:
                    daysUntilWarmer[i] = j - i
                    break
        
        return daysUntilWarmer
    
    def DaysUntilWarmerV2(self, temperatures):
        days = len(temperatures)
        daysUntilWarmer = [0] * days

        # Monotonic stack
        stack = []

        for i in range(days):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                daysUntilWarmer[stack[-1]] = i - stack[-1]
                stack.pop()

            stack.append(i)

        return daysUntilWarmer

    def DaysUntilWarmer(self, temperatures):
        return self.DaysUntilWarmerV2(temperatures)


if __name__ == "__main__":
    solution = Solution()

    temperatures = [45, 50, 40, 60, 55]
    expectedOutput = [1, 2, 1, 0, 0]
    output = solution.DaysUntilWarmer(temperatures)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    temperatures = [80, 75, 85, 90, 60]
    expectedOutput = [2, 1, 1, 0, 0]
    output = solution.DaysUntilWarmer(temperatures)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    temperatures = [32, 32, 32, 32, 32]
    expectedOutput = [0, 0, 0, 0, 0]
    output = solution.DaysUntilWarmer(temperatures)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()
