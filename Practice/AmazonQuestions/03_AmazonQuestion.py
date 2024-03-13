# Amazon Web Services has n servers. The cache optimization power of the ith
# server is power[i]. The cache optimization power of a group of contiguous
# servers [l, r] is defined as:
# 
# Power_lr = min_(l <= i <= r)(power[i]) * sum(power[i]) from i = l to r
# 
# Find the sum of Power_lr for each possible contiguous group of servers.
# Since the answer can be very large, return the answer modulo (10 ^ 9 + 7).
#     
# Example
# power = [2, 3, 2, 1]
# 
# There are 4 servers. The powers of contiguous groups are:
# Power_lr[0, 0] = min([2]) * sum([2])
# Power_lr[0, 1] = min([2, 3]) * sum([2, 3])
# ...
# Power_lr[0, 3] = min([2, 3, 2, 1]) * sum([2, 3, 2, 1])
# ...
# Power_lr[3,3] = min([1]) * sum([1])
# 
# Implement a function to compute the sum of Power_lr for each possible contiguous group of servers

def SumOfPowers(power):
    n = len(power)

    sumOfPowers = 0

    for i in range(n):
        for j in range(i + 1, n + 1):
            sumOfPowers += min(power[i:j]) * sum(power[i:j])

    return sumOfPowers % (10 ** 9 + 7)

if __name__ == "__main__":
    # Example 1
    power = [2, 3, 2, 1]
    expectedOutput = 69
    output = SumOfPowers(power)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    power = [1, 3, 4]
    expectedOutput = 59
    output = SumOfPowers(power)
    print(output, expectedOutput, output == expectedOutput)