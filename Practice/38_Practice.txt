# 211. Design Add and Search Words Data Structure (Medium)
# Design a data structure that supports adding new words and finding if a
# string matches any previously added string.
# 
# Implement the WordDictionary class:
# 
# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure
# that matches word or false otherwise. word may contain dots '.' where dots
# can be matched with any letter.
# 
# Example:
#   Input
#     ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
#     [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# 
#   Output
#     [null,null,null,null,false,true,true,true]
# 
# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True


from collections import deque

class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isWord = True

    def search(self, word: str) -> bool:
        def dfsSearch(node, word, startIndex=0):
            for i in range(startIndex, len(word)):
                c = word[i]

                if c == ".":
                    for child in node.children.values():
                        if dfsSearch(child, word, i + 1):
                            return True
                    return False
                else:
                    if c not in node.children:
                        return False
                    node = node.children[c]
            return node.isWord
        
        return dfsSearch(self.root, word)

if __name__ == "__main__":
    # Example
    wordDictionary = WordDictionary()
    wordDictionary.addWord("bad")
    wordDictionary.addWord("dad")
    wordDictionary.addWord("mad")
    print(wordDictionary.search("pad"), False)
    print(wordDictionary.search("bad"), True)
    print(wordDictionary.search(".ad"), True)
    print(wordDictionary.search("b.."), True)