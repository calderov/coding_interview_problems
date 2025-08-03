# Colorful Numbers
# https://tutorialhorizon.com/algorithms/colorful-numbers/

# Objective: Given a number, find out whether it is colorful.

# Colorful Number: When in a given number, the product of every contiguous sub-sequence is different. That number is called a Colorful Number. 

# Example 1:
#   Given Number : 3245
#   Output: True
#   Number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245.
#   this number is a colorful number, since product of every digit of a sub-sequence are different.
#   That is, 3 2 4 5 (3*2)=6 (2*4)=8 (4*5)=20, (3*2*4)= 24 (2*4*5)= 40

# Example 2:
#   Given Number : 326
#   Output: False
#   326 is not a colorful number as it generates 3 2 6 (3*2)=6 (2*6)=12.

# Complexity:
# Time: O(n^2) where n is the lenght of the number in digits
# Space: O(n^2)
def isColorful(number):
    digits = str(number)
    products = set()
    n = len(digits)

    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= int(digits[j])
            if product in products:
                return False
            products.add(product)

    return True


if __name__ == "__main__":
    # Example 1
    number = 3245
    expected = True
    output = isColorful(number)

    print(number)
    print(expected)
    print(output)
    print(output == expected)

    print()

    # Example 2
    number = 326
    expected = False
    output = isColorful(number)

    print(number)
    print(expected)
    print(output)
    print(output == expected)

    print()
    