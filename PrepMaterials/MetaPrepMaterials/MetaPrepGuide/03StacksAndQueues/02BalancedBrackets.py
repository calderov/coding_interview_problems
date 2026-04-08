# Balanced Brackets
# https://www.hackerrank.com/challenges/balanced-brackets/problem

def isBalancedBrackets(s):
    brackets = {"(":")", "{":"}", "[":"]"}
    stack = []

    for c in s:
        if c in brackets:
            stack.append(brackets[c])
        else:
            if stack and c == stack[-1]:
                stack.pop()
            else:
                return False
    
    return True
    
if __name__=="__main__":
    # Example 1
    s = "(({{{[]}}}))"
    expected = True
    output = isBalancedBrackets(s)
    
    print(s)
    print(expected)
    print(output)
    print(output == expected)

    print()

    # Example 2
    s = "(({{]}}}))"
    expected = False
    output = isBalancedBrackets(s)
    
    print(s)
    print(expected)
    print(output)
    print(output == expected)

