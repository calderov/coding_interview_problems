# Arrays: Left Rotation
# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem

# Complexity
# Time: O(dn) -> O(n)
# Space: O(n)
def rotLeftNaive(a, d):
    if not a:
        return []

    n = len(a)
    rotated = [0] * n

    for i in range(n):
        j = (i - d + n) % n
        rotated[j] = a[i]

    return rotated

def reverseInplace(a, low, high):
    if not a or low >= high or low < 0 or high >= len(a):
        return a

    while low < high:
        a[low], a[high] = a[high], a[low]
        low += 1
        high -= 1

# Time complexity: O(n)
# Space complexity: O(1)
def rotLeftInPlace(a, d):
    if not a:
        return a

    n = len(a)
    d = d % n

    if d == 0:
        return a

    reverseInplace(a, 0, d - 1)
    reverseInplace(a, d, n - 1)
    reverseInplace(a, 0, n - 1)

    return a

def rotLeft(a, d):
    return rotLeftInPlace(a, d)

if __name__ == "__main__":
    # Example 1
    a = [1,2,3,4,5]
    d = 4
    expected = [5,1,2,3,4]
    output = rotLeft(a, d)

    print(a,d)
    print(expected)
    print(output)
    print(output == expected)
    print()

    # Example 2
    a = [1,2,3,4,5]
    d = 3
    expected = [4,5,1,2,3]
    output = rotLeft(a, d)

    print(a,d)
    print(expected)
    print(output)
    print(output == expected)
    print()

    # Example 3
    a = [1,2,3,4,5]
    d = 5003
    expected = [4,5,1,2,3]
    output = rotLeft(a, d)

    print(a,d)
    print(expected)
    print(output)
    print(output == expected)
    print()
