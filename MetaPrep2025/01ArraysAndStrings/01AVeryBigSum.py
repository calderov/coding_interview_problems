# A Very Big Sum
# https://www.hackerrank.com/challenges/a-very-big-sum/problem

def aVeryBigSum(ar):
    bigSum = 0
    for i in ar:
        bigSum += i
    return bigSum

if __name__=="__main__":
    nums = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
    expected = 5000000015
    output = aVeryBigSum(nums)

    print(expected)
    print(output)
    print(expected == output)