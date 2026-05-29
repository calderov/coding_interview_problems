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

    for word in words:
        if currentLineWidth + len(word) <= maxWidth:
            currentLine.append(word)
            currentLineWidth += len(word)
        else:
            if currentLine[-1] == " ":
                currentLine.pop()

            lines.append(currentLine)
            currentLine = [word]
            currentLineWidth = len(word)

        if currentLineWidth + 1 <= maxWidth:
            currentLine.append(" ")
            currentLineWidth += 1

    if currentLine:
        if currentLine[-1] == " ":
            currentLine.pop()
        lines.append(currentLine)

    return lines

def JustifyLeft(line, maxWidth):
    lineWidth = sum(len(word) for word in line)
    rightPadding = maxWidth - lineWidth
    line.append(" " * rightPadding)
    return "".join(line)

def JustifyRight(line, maxWidth):
    spaceIndexes = [[i, 1] for i in range(len(line)) if line[i] == " "]
    lineWidth = sum([len(word) for word in line])

    i = 0
    while lineWidth < maxWidth:
        spaceIndexes[i][1] += 1
        lineWidth += 1
        i += 1

        if i == len(spaceIndexes):
            i = 0

    for index, padding in spaceIndexes:
        line[index] = " " * padding

    return "".join(line)

# Time: O(n * maxWidth)
# Space: O(n * maxWidth)
def JustifyText(words, maxWidth):
    # Split words into lines of at most maxWidht (including single space separation between words)
    lines = SplitLines(words, maxWidth)

    for i in range(len(lines)):
        line = lines[i]

        # If the current line is the last line in lines or contains a single word, justify left
        if i == len(lines) - 1 or len(line) == 1:
            line = JustifyLeft(line, maxWidth)

        # Otherwise, justify right
        else:
            line = JustifyRight(line, maxWidth)

        lines[i] = line

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