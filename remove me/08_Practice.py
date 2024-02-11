# Given an integer number n, return True if n is a power of 3

def IsPowerOfThree(n):
    if n < 1:
        return False
    
    while n % 3 == 0:
        n = n // 3

    return n == 1

if __name__ == "__main__":
    print(1, IsPowerOfThree(1))
    print(3, IsPowerOfThree(3))
    print(9, IsPowerOfThree(9))
    print(27, IsPowerOfThree(27))
    print(81, IsPowerOfThree(81))
    print()
    print(0, IsPowerOfThree(0))
    print(6, IsPowerOfThree(6))
    print(12, IsPowerOfThree(12))
    print(18, IsPowerOfThree(18))

    