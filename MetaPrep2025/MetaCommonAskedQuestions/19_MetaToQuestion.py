# 691. Stickers to Spell Word
# We are given n different types of stickers. Each sticker has a lowercase
# English word on it.
# 
# You would like to spell out the given string target by cutting individual
# letters from your collection of stickers and rearranging them. You can use
# each sticker more than once if you want, and you have infinite quantities
# of each sticker.
# 
# Return the minimum number of stickers that you need to spell out target. If
# the task is impossible, return -1.
# 
# Note: In all test cases, all words were chosen randomly from the 1000 most
# common US English words, and target was chosen as a concatenation of two
# random words.
# 
# Example 1:
# Input: stickers = ["with","example","science"], target = "thehat"
# Output: 3
# Explanation: We can use 2 "with" stickers, and 1 "example" sticker.
#              After cutting and rearrange the letters of those stickers, we
#              can form the target "thehat". Also, this is the minimum number
#              of stickers necessary to form the target string.
# 
# Example 2:
# Input: stickers = ["notice","possible"], target = "basicbasic"
# Output: -1
# Explanation: We cannot form the target "basicbasic" from cutting letters
#              from the given stickers.
# 
# Constraints:
# - n == stickers.length
# - 1 <= n <= 50
# - 1 <= stickers[i].length <= 10
# - 1 <= target.length <= 15
# - stickers[i] and target consist of lowercase English letters.

from collections import deque

def canBeSpelled(stickers, s):
    alphabet = set(list("".join(stickers)))
    targetChars = set(list(s))
    return len(targetChars.difference(alphabet)) == 0

def getStickerMaps(stickers):
    stickerMaps = []
    for sticker in stickers:
        stickerMap = {}
        for c in sticker:
            stickerMap[c] = stickerMap.get(c, 0) + 1
        stickerMaps.append(stickerMap)
    return stickerMaps

def applyStickerMap(stickerMap, s):
    seen = {}
    nextS = []

    for c in s:
        if c not in stickerMap or seen.get(c, 0) >= stickerMap[c]:
            nextS.append(c)
        seen[c] = seen.get(c, 0) + 1
    
    return "".join(nextS)

def stickersToSpellWord(stickers, target):
    if not target:
        return 0

    if not canBeSpelled(stickers, target):
        return -1
    
    stickerMaps = getStickerMaps(stickers)
    pending = deque([(target, 0)])
    visited = set()

    while pending:
        s, usedStickers = pending.popleft()
        visited.add(s)

        if s == "":
            return usedStickers

        for stickerMap in stickerMaps:
            nextS = applyStickerMap(stickerMap, s)
            if nextS not in visited:
                pending.append((nextS, usedStickers + 1))
    
    return -1

if __name__ == "__main__":
    # Example 1
    stickers = ["with","example","science"]
    target = "thehat"
    expectedOutput = 3
    output = stickersToSpellWord(stickers, target)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    stickers = ["notice","possible"]
    target = "basicbasic"
    expectedOutput = -1
    output = stickersToSpellWord(stickers, target)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    stickers = ["11112222333","44455"]
    target = "111222233311113332224411155"
    expectedOutput = 4
    output = stickersToSpellWord(stickers, target)
    print(output, expectedOutput, output == expectedOutput)
