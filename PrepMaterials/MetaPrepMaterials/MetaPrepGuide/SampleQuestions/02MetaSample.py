# Question 2: Look and Say

# Implement a function that outputs the Look and Say sequence:
# 1
# 11
# 21
# 1211
# 111221
# 312211
# 13112221
# 1113213211
# 31131211131221
# 13211311123113112211

def nextNumber(number):
    digits = [int(d) for d in str(number)]
    
    # Fill a stack with records of the form [t, d]
    # where t is the number of times that a digit d
    # repeats before changing. E.g [2, 1] should be
    # read as: "There are two instances of one", or
    # in terms of look and say "two one".
    stack = [[0, digits[0]]]

    for d in digits:
        if d == stack[-1][1]:
            stack[-1][0] += 1
        else:
            stack.append([1, d])
    
    # Extract next number from stack
    newDigits = []

    for c, d in stack:
        newDigits.append(str(c))
        newDigits.append(str(d))

    return int("".join(newDigits))

def lookAndSay(seed, iterations):
    number = seed
    
    for i in range(iterations):
        print(number)
        number = nextNumber(number)

if __name__=="__main__":
    start = 1
    lookAndSay(1, 8)
    