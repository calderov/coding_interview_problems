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

def GetNextWarmDays(temperatures):
    days = [0] * len(temperatures)

    for i in range(len(temperatures) - 1):
        for j in range(i + 1, len(temperatures)):
            if temperatures[j] > temperatures[i]:
                days[i] = j - i
                break

    return days

def GetNextWarmDaysV2(temperatures):
    days = [0] * len(temperatures)
    stack = []

    for i in range(len(temperatures)):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            days[stack[-1]] = i - stack[-1]
            stack.pop()
        stack.append(i)

    return days


if __name__ == "__main__":
    temperatures = [70, 73, 75, 71, 69, 72, 76, 73]
    expectedOutput = [1, 1, 4, 2, 1, 1, 0, 0]
    output = GetNextWarmDaysV2(temperatures)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
