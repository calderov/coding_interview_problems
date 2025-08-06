# Question 3: Edit Distance
# Write a function that returns whether two words are exactly "one edit" away using the following signature:
# bool OneEditApart(string s1, string s2);
# An edit is:

#     Inserting one character anywhere in the word (including at the beginning and end)
#     Removing one character
#     Replacing one character

# Examples:
# OneEditApart("cat", "dog") = false
# OneEditApart("cat", "cats") = true
# OneEditApart("cat", "cut") = true
# OneEditApart("cat", "cast") = true
# OneEditApart("cat", "at") = true
# OneEditApart("cat", "act") = false


def OneEditApart(s1, s2):

    if len(s1) > len(s2):
        temp = s1
        s1 = s2
        s2 = temp

    if len(s2) - len(s1) > 1:
        return False

    edits = 0
    i = 0
    j = 0

    while i < len(s1):
        if s1[i] != s2[j]:
            if edits:
                return False
            edits += 1
            if len(s2) > len(s1):
                i -= 1
        i += 1
        j += 1

    if len(s2) > len(s1) and not edits:
        edits += 1

    return edits == 1

if __name__ == "__main__":
    s1 = "cat"
    s2 = "dog"
    expectedOutput = True
    output = OneEditApart(s1, s2)
    
    print(s1)
    print(s2)
    print(expectedOutput == output)

    print()
    
    s1 = "cat"
    s2 = "cats"
    expectedOutput = True
    output = OneEditApart(s1, s2)
    
    print(s1)
    print(s2)
    print(expectedOutput == output)

    print()
    
    s1 = "scat"
    s2 = "cat"
    expectedOutput = True
    output = OneEditApart(s1, s2)
    
    print(s1)
    print(s2)
    print(expectedOutput == output)

    print()
    
    s1 = "tttt"
    s2 = "ttatt"
    expectedOutput = True
    output = OneEditApart(s1, s2)
    
    print(s1)
    print(s2)
    print(expectedOutput == output)