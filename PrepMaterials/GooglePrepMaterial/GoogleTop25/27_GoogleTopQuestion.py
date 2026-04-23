# Text Justification
# HARD
# Description

# Given an array of strings words and a width maxWidth, format the text such that each line has exactly
# maxWidth characters and is fully (left and right) justified.

# You should pack your words in a greedy approach; that is, pack as many words as you can in each line.
# Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a
# line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

# For the last line of text, it should be left-justified, and no extra space is inserted between words.

# Note:

#     A word is defined as a character sequence consisting of non-space characters only.
#     Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
#     The input array words contains at least one word.

# Example 1:
# Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
# Output:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]

# Example 2:
# Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
# Output:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
# Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
# Note that the second line is also left-justified because it contains only one word.

# Example 3:
# Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
# Output:
# [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]

# Constraints:
#     1 <= words.length <= 300
#     1 <= words[i].length <= 20
#     words[i] consists of only English letters and symbols.
#     1 <= maxWidth <= 100
#     words[i].length <= maxWidth

def SplitLines(words, maxWidth):
    lines = []
    currentLine = []
    currentLineWidth = 0

    # For each word
    for word in words:
        # If the current line is still shorter than the max width, append it to the lines list
        if currentLineWidth + len(word) <= maxWidth:
            currentLine.append(word)
            currentLineWidth += len(word)
       
        # Otherwise remove the trailing space at the end of the current line if present,
        # append the current line to the lines list, and use the current word to redefine
        # a new current line and current line width.
        else:
            if currentLine[-1] == " ":
                currentLine.pop()
            
            lines.append(currentLine)
            currentLine = [word]
            currentLineWidth = len(word)

        # If a space can be appended to the current line, do it
        if currentLineWidth + 1 <= maxWidth:
            currentLine.append(" ")
            currentLineWidth += 1

    # If there is still a current line under construction after traversing all the words, append it
    # to the lines list, just make sure of removing any trailing space.
    if currentLine:
        if currentLine[-1] == " ":
            currentLine.pop()

        lines.append(currentLine)

    return lines

def JustifyLeft(line, maxWidth):
    characters = sum([len(word) for word in line])
    rightPadding = maxWidth - characters
    line.append(" " * rightPadding)
    return "".join(line)
    
def JustifyRight(line, maxWidth):
    spaceIndexes = [[i, 1] for i in range(len(line)) if line[i] == " "]

    spaces = len(spaceIndexes)
    characters = sum([len(word) for word in line if word != " "])

    lineWidth = characters + spaces

    i = 0
    while lineWidth < maxWidth:
        index, count = spaceIndexes[i]
        spaceIndexes[i] = [index, count + 1]
        lineWidth += 1
        i += 1

        if i == len(spaceIndexes):
            i = 0

    for index, count in spaceIndexes:
        line[index] = " " * count

    return "".join(line)

# Time: O(n * maxWidth)
# Space: O(n * maxWidth)
def JustifyText(words, maxWidth):
    lines = SplitLines(words, maxWidth)

    for i in range(len(lines)):
        currentLine = lines[i]

        # Case 1: If this is the last line or the line only has one word, justify left
        if i == len(lines) - 1 or len(currentLine) == 1:
            currentLine = JustifyLeft(currentLine, maxWidth)
        
        # Case 2: This is a regular line, justify right
        else:
            currentLine = JustifyRight(currentLine, maxWidth)

        lines[i] = currentLine
    
    return lines

if __name__ == "__main__":
    # Example 1:
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    expected = [
       "This    is    an",
       "example  of text",
       "justification.  "
    ]
    output = JustifyText(words, maxWidth)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 2:
    words = ["What","must","be","acknowledgment","shall","be"]
    maxWidth = 16
    expected = [
      "What   must   be",
      "acknowledgment  ",
      "shall be        "
    ]
    output = JustifyText(words, maxWidth)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 3:
    words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
    maxWidth = 20
    expected = [
      "Science  is  what we",
      "understand      well",
      "enough to explain to",
      "a  computer.  Art is",
      "everything  else  we",
      "do                  "
    ]
    output = JustifyText(words, maxWidth)
    print(expected)
    print(output)
    print(expected == output)
    print()