# Arrays: Left Rotation
# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem

# Complexity
# Time: O(dn) -> O(n)
# Space: O(n)
def rotLeft(a, d):
    n = len(a)
    rotated = [0] * n

    for i in range(n):
        j = (i - d + n) % n
        rotated[j] = a[i]

    return rotated

if __name__ == "__main__":
    a = [1,2,3,4,5]
    d = 4
    expected = [5,1,2,3,4]
    output = rotLeft(a, d)

    print(a,d)
    print(expected)
    print(output)
    print(output == expected)

